"""
This module contains the code to get weather data from
Visual Crossing API.
See: https://www.visualcrossing.com/
"""
from __future__ import annotations

import abc
import datetime
import json
import logging

from typing import List, Any, Dict
from urllib.request import urlopen

import aiohttp

from .const import CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, VISUALCROSSING_BASE_URL
from .data import ForecastData, ForecastDailyData, ForecastHourlyData

UTC = datetime.timezone.utc

_LOGGER = logging.getLogger(__name__)

class VisualCrossingException(Exception):
    """Exception thrown if failing to access API."""


class VisualCrossingAPIBase:
    """
    Baseclass to use as dependency injection pattern for easier
    automatic testing
    """

    @abc.abstractmethod
    def fetch_data(self, api_key: str, latitude: float, longitude: float) -> Dict[str, Any]:
        """Override this"""
        raise NotImplementedError(
            "users must define fetch_data to use this base class"
        )

    @abc.abstractmethod
    async def async_fetch_data(
        api_key: str, latitude: float, longitude: float
    ) -> Dict[str, Any]:
        """Override this"""
        raise NotImplementedError(
            "users must define fetch_data to use this base class"
        )

class VisualCrossingAPI(VisualCrossingAPIBase):
    """Default implementation for WeatherFlow api"""

    def __init__(self) -> None:
        """Init the API with or without session"""
        self.session = None

    def fetch_data(self, api_key: str, latitude: float, longitude: float) -> Dict[str, Any]:
        """Get data from API."""
        api_url =f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}?unitGroup=metric&key={api_key}&contentType=json"

        response = urlopen(api_url)
        data = response.read().decode("utf-8")
        json_data = json.loads(data)

        return json_data

    async def async_fetch_data(self, api_key: str, latitude: float, longitude: float) -> Dict[str, Any]:
        """Get data from API."""
        api_url =f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}?unitGroup=metric&key={api_key}&contentType=json"

        is_new_session = False
        if self.session is None:
            self.session = aiohttp.ClientSession()
            is_new_session = True

        async with self.session.get(api_url) as response:
            if response.status != 200:
                if is_new_session:
                    await self.session.close()
                raise VisualCrossingException(
                    f"Failed to access Visual Crossing API with status code {response.status}"
                )
            data = await response.text()
            if is_new_session:
                await self.session.close()
            return json.loads(data)

class VisualCrossing:
    """
    Class that uses the weather API from Visual Crossing
    to retreive Weather Data for supplied Latitude and
    longitude location
    """

    def __init__(
        self,
        api_key: str,
        latitude: float,
        longitude: float,
        session: aiohttp.ClientSession = None,
        api: VisualCrossingAPIBase =VisualCrossingAPI(),
    ) -> None:
        self._api_key = api_key
        self._latitude = latitude
        self._longitude = longitude
        self._api = api
        self._json_data = None

        if session:
            self._api.session = session

    def fetch_data(self) -> List[ForecastData]:
        """Returns a list of weather data."""

        if self._json_data is None:
            self._json_data = self._api.fetch_data(self._api_key, self._latitude, self._longitude)

        return _fetch_data(self._json_data)

    async def async_fetch_data(self) -> List[ForecastData]:
        """Returns a list of weather data."""

        if self._json_data is None:
            self._json_data = await self._api.async_fetch_data(self._api_key, self._latitude, self._longitude)

        return _fetch_data(self._json_data)

def _fetch_data(api_result: dict) -> List[ForecastData]:
    """Converts result from API to ForecastData List."""

    current_conditions: ForecastData = _get_current_data(api_result)

# pylint: disable=R0914, R0912, W0212, R0915
def _get_current_data(api_result: dict) -> List[ForecastData]:
    """Converts results from API to WeatherFlowForecast list"""

    item = api_result["currentConditions"]

    valid_time = datetime.datetime.utcfromtimestamp(item["datetimeEpoch"]).replace(tzinfo=UTC)
    condition = item.get("conditions", None)
    cloudcover = item.get("cloudcover", None)
    icon = item.get("icon", None)
    temperature = item.get("temp", None)
    dew_point = item.get("dew", None)
    apparent_temperature = item.get("feelslike", None)
    precipitation = item.get("precip", None)
    precipitation_probability = item.get("precipprob", None)
    humidity = item.get("humidity", None)
    solarradiation = item.get("solarradiation", None)
    visibility = item.get("visibility", None)
    pressure = item.get("pressure", None)
    uv_index = item.get("uvindex", None)
    wind_speed = item.get("windspeed", None)
    wind_gust_speed = item.get("windgust", None)
    wind_bearing = item.get("winddir", None)

    current_condition = ForecastData(
        valid_time,
        apparent_temperature,
        condition,
        cloudcover,
        dew_point,
        humidity,
        icon,
        precipitation,
        precipitation_probability,
        pressure,
        solarradiation,
        temperature,
        visibility,
        uv_index,
        wind_bearing,
        wind_gust_speed,
        wind_speed,
    )

    return current_condition


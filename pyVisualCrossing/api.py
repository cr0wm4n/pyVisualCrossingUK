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

from .const import SUPPORTED_LANGUAGES, VISUALCROSSING_BASE_URL
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
    def fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> Dict[str, Any]:
        """Override this"""
        raise NotImplementedError("users must define fetch_data to use this base class")

    @abc.abstractmethod
    async def async_fetch_data(
        api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> Dict[str, Any]:
        """Override this"""
        raise NotImplementedError("users must define fetch_data to use this base class")


class VisualCrossingAPI(VisualCrossingAPIBase):
    """Default implementation for WeatherFlow api"""

    def __init__(self) -> None:
        """Init the API with or without session"""
        self.session = None

    def fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> Dict[str, Any]:
        """Get data from API."""
        api_url = f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}/today/next{days}days?unitGroup=metric&key={api_key}&contentType=json&iconSet=icons2&lang={language}"
        _LOGGER.debug("URL: %s", api_url)

        response = urlopen(api_url)
        data = response.read().decode("utf-8")
        json_data = json.loads(data)

        return json_data

    async def async_fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> Dict[str, Any]:
        """Get data from API."""
        api_url = f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}/today/next{days}days?unitGroup=metric&key={api_key}&contentType=json&iconSet=icons2&lang={language}"

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
        days: int = 14,
        language: str = "en",
        session: aiohttp.ClientSession = None,
        api: VisualCrossingAPIBase = VisualCrossingAPI(),
    ) -> None:
        self._api_key = api_key
        self._latitude = latitude
        self._longitude = longitude
        self._days = days
        self._language = language
        self._api = api
        self._json_data = None

        if days > 14:
            self._days = 14

        if session:
            self._api.session = session

        if language not in SUPPORTED_LANGUAGES:
            self._language = "en"

    def fetch_data(self) -> List[ForecastData]:
        """Returns a list of weather data."""

        if self._json_data is None:
            self._json_data = self._api.fetch_data(
                self._api_key,
                self._latitude,
                self._longitude,
                self._days,
                self._language,
            )

        return _fetch_data(self._json_data)

    async def async_fetch_data(self) -> List[ForecastData]:
        """Returns a list of weather data."""

        if self._json_data is None:
            self._json_data = await self._api.async_fetch_data(
                self._api_key,
                self._latitude,
                self._longitude,
                self._days,
                self._language,
            )

        return _fetch_data(self._json_data)


def _fetch_data(api_result: dict) -> List[ForecastData]:
    """Converts result from API to ForecastData List."""

    # Add Current Condition Data
    weather_data: ForecastData = _get_current_data(api_result)

    forecast_daily = []
    forecast_hourly = []

    # Loop Through Records and add Daily and Hourly Forecast Data
    for item in api_result["days"]:
        valid_time = datetime.datetime.utcfromtimestamp(item["datetimeEpoch"]).replace(
            tzinfo=UTC
        )
        condition = item.get("conditions", None)
        cloudcover = item.get("cloudcover", None)
        icon = item.get("icon", None)
        temperature = item.get("tempmax", None)
        temp_low = item.get("tempmin", None)
        dew_point = item.get("dew", None)
        apparent_temperature = item.get("feelslike", None)
        precipitation = item.get("precip", None)
        precipitation_probability = item.get("precipprob", None)
        humidity = item.get("humidity", None)
        pressure = item.get("pressure", None)
        uv_index = item.get("uvindex", None)
        wind_speed = item.get("windspeed", None)
        wind_gust_speed = item.get("windgust", None)
        wind_bearing = item.get("winddir", None)

        day_data = ForecastDailyData(
            valid_time,
            temperature,
            temp_low,
            apparent_temperature,
            condition,
            icon,
            cloudcover,
            dew_point,
            humidity,
            precipitation_probability,
            precipitation,
            pressure,
            wind_bearing,
            wind_speed,
            wind_gust_speed,
            uv_index,
        )
        forecast_daily.append(day_data)

        # Add Hourly data for this day
        for row in item["hours"]:
            now = datetime.datetime.now().replace(tzinfo=UTC)
            valid_time = datetime.datetime.utcfromtimestamp(
                row["datetimeEpoch"]
            ).replace(tzinfo=UTC)
            if valid_time > now:
                condition = row.get("conditions", None)
                cloudcover = row.get("cloudcover", None)
                icon = row.get("icon", None)
                temperature = row.get("temp", None)
                dew_point = row.get("dew", None)
                apparent_temperature = row.get("feelslike", None)
                precipitation = row.get("precip", None)
                precipitation_probability = row.get("precipprob", None)
                humidity = row.get("humidity", None)
                pressure = row.get("pressure", None)
                uv_index = row.get("uvindex", None)
                wind_speed = row.get("windspeed", None)
                wind_gust_speed = row.get("windgust", None)
                wind_bearing = row.get("winddir", None)

                hour_data = ForecastHourlyData(
                    valid_time,
                    temperature,
                    apparent_temperature,
                    condition,
                    cloudcover,
                    icon,
                    dew_point,
                    humidity,
                    precipitation,
                    precipitation_probability,
                    pressure,
                    wind_bearing,
                    wind_gust_speed,
                    wind_speed,
                    uv_index,
                )
                forecast_hourly.append(hour_data)

    weather_data.forecast_daily = forecast_daily
    weather_data.forecast_hourly = forecast_hourly

    return weather_data


# pylint: disable=R0914, R0912, W0212, R0915
def _get_current_data(api_result: dict) -> List[ForecastData]:
    """Converts results from API to WeatherFlowForecast list"""

    item = api_result["currentConditions"]

    valid_time = datetime.datetime.utcfromtimestamp(item["datetimeEpoch"]).replace(
        tzinfo=UTC
    )
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
    location = api_result.get("address", None)

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
        location,
    )

    return current_condition

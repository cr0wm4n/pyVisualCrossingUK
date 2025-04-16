"""This module contains the code to get weather data from Visual Crossing API.

See: https://www.visualcrossing.com/.
"""
from __future__ import annotations

import abc
import datetime
from datetime import timezone
import json
import logging

from typing import Any
import urllib.request

import aiohttp

from .const import DATE_FORMAT, DATE_TIME_FORMAT, SUPPORTED_LANGUAGES, VISUALCROSSING_BASE_URL
from .data import ForecastData, ForecastDailyData, ForecastHourlyData

UTC = datetime.timezone.utc

_LOGGER = logging.getLogger(__name__)


class VisualCrossingException(Exception):
    """Exception thrown if failing to access API."""


class VisualCrossingBadRequest(Exception):
    """Request is invalid."""


class VisualCrossingUnauthorized(Exception):
    """Unauthorized API Key."""


class VisualCrossingTooManyRequests(Exception):
    """Too many daily request for the current plan."""


class VisualCrossingInternalServerError(Exception):
    """Visual Crossing servers encounter an unexpected error."""


class VisualCrossingAPIBase:
    """Baseclass to use as dependency injection pattern for easier automatic testing."""

    @abc.abstractmethod
    def fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> dict[str, Any]:
        """Override this."""
        raise NotImplementedError("users must define fetch_data to use this base class")

    @abc.abstractmethod
    async def async_fetch_data(
        api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> dict[str, Any]:
        """Override this."""
        raise NotImplementedError("users must define fetch_data to use this base class")


class VisualCrossingAPI(VisualCrossingAPIBase):
    """Default implementation for WeatherFlow api."""

    def __init__(self) -> None:
        """Init the API with or without session."""
        self.session = None

    def fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> dict[str, Any]:
        """Get data from API."""
        api_url = f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}/today/next{days}days?unitGroup=uk&key={api_key}&contentType=json&iconSet=icons2&lang={language}"
        _LOGGER.debug("URL: %s", api_url)

        try:
            response = urllib.request.urlopen(api_url)
            data = response.read().decode("utf-8")
            json_data = json.loads(data)

            return json_data
        except urllib.error.HTTPError as errh:
            if errh.code == 400:
                raise VisualCrossingBadRequest(
                    "400 BAD_REQUEST Requests is invalid in some way (invalid dates, bad location parameter etc)."
                )
            elif errh.code == 401:
                raise VisualCrossingUnauthorized(
                    "401 UNAUTHORIZED The API key is incorrect or your account status is inactive or disabled."
                )
            elif errh.code == 429:
                raise VisualCrossingTooManyRequests(
                    "429 TOO_MANY_REQUESTS Too many daily request for the current plan."
                )
            elif errh.code == 500:
                raise VisualCrossingInternalServerError(
                    "500 INTERNAL_SERVER_ERROR Visual Crossing servers encounter an unexpected error."
                )

        return None

    async def async_fetch_data(
        self, api_key: str, latitude: float, longitude: float, days: int, language: str
    ) -> dict[str, Any]:
        """Get data from API."""
        api_url = f"{VISUALCROSSING_BASE_URL}{latitude},{longitude}/today/next{days}days?unitGroup=uk&key={api_key}&contentType=json&iconSet=icons2&lang={language}"

        is_new_session = False
        if self.session is None:
            self.session = aiohttp.ClientSession()
            is_new_session = True

        async with self.session.get(api_url) as response:
            if response.status != 200:
                if is_new_session:
                    await self.session.close()
                if response.status == 400:
                    raise VisualCrossingBadRequest(
                        "400 BAD_REQUEST Requests is invalid in some way (invalid dates, bad location parameter etc)."
                    )
                if response.status == 401:
                    raise VisualCrossingUnauthorized(
                        "401 UNAUTHORIZED The API key is incorrect or your account status is inactive or disabled."
                    )
                if response.status == 429:
                    raise VisualCrossingTooManyRequests(
                        "429 TOO_MANY_REQUESTS Too many daily request for the current plan."
                    )
                if response.status == 500:
                    raise VisualCrossingInternalServerError(
                        "500 INTERNAL_SERVER_ERROR Visual Crossing servers encounter an unexpected error."
                    )

            data = await response.text()
            if is_new_session:
                await self.session.close()
            return json.loads(data)


class VisualCrossing:
    """Class that uses the weather API from Visual Crossing to retreive Weather Data."""

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
        """Return data from Weather API."""
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

    def fetch_data(self) -> list[ForecastData]:
        """Return list of weather data."""

        self._json_data = self._api.fetch_data(
            self._api_key,
            self._latitude,
            self._longitude,
            self._days,
            self._language,
        )

        return _fetch_data(self._json_data)

    async def async_fetch_data(self) -> list[ForecastData]:
        """Return list of weather data."""

        self._json_data = await self._api.async_fetch_data(
            self._api_key,
            self._latitude,
            self._longitude,
            self._days,
            self._language,
        )

        return _fetch_data(self._json_data)


def _fetch_data(api_result: dict) -> list[ForecastData]:
    """Return result from API to ForecastData List."""

    # Return nothing af the Request for data fails
    if api_result is None:
        return None

    # Add Current Condition Data
    weather_data: ForecastData = _get_current_data(api_result)

    forecast_daily = []
    forecast_hourly = []

    # Loop Through Records and add Daily and Hourly Forecast Data
    for item in api_result["days"]:
        day_str = item["datetime"]
        day_obj = datetime.datetime.strptime(day_str, DATE_FORMAT).astimezone(timezone.utc)
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
            day_obj,
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
            now = datetime.datetime.now(timezone.utc)
            hour = row["datetime"]
            day_hour_obj = datetime.datetime.strptime(f"{day_str} {hour}", DATE_TIME_FORMAT).astimezone(timezone.utc)
            if day_hour_obj > now:
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
                    day_hour_obj,
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
def _get_current_data(api_result: dict) -> list[ForecastData]:
    """Return WeatherFlowForecast list from API."""

    item = api_result["currentConditions"]

    day_str = datetime.datetime.today().strftime(DATE_FORMAT)
    hour = item["datetime"]
    day_hour_obj = datetime.datetime.strptime(f"{day_str} {hour}", DATE_TIME_FORMAT).astimezone(timezone.utc)
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
    description = api_result.get("description", None)

    current_condition = ForecastData(
        day_hour_obj,
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
        description,
    )

    return current_condition

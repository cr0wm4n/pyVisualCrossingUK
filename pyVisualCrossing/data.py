"""Holds the Data Classes for Visual Crossing Wrapper"""

from __future__ import annotations
from datetime import datetime
from typing import List


class ForecastData:
    """Class to hold forecast data."""

    # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        apparent_temperature: float,
        condition: str,
        cloud_cover: int,
        dew_point: float,
        humidity: int,
        icon: str,
        precipitation: float,
        precipitation_probability: int,
        pressure: float,
        solarradiation: float,
        temperature: float,
        visibility: int,
        uv_index: int,
        wind_bearing: int,
        wind_gust_speed: float,
        wind_speed: float,
        location_name: str,
        forecast_daily: ForecastDailyData = None,
        forecast_hourly: ForecastHourlyData = None,
    ) -> None:
        """Constructor"""
        self._datetime = datetime
        self._apparent_temperature = apparent_temperature
        self._condition = condition
        self._cloud_cover = cloud_cover
        self._dew_point = dew_point
        self._humidity = humidity
        self._icon = icon
        self._precipitation = precipitation
        self._precipitation_probability = precipitation_probability
        self._pressure = pressure
        self._solarradiation = solarradiation
        self._visibility = visibility
        self._temperature = temperature
        self._uv_index = uv_index
        self._wind_bearing = wind_bearing
        self._wind_gust_speed = wind_gust_speed
        self._wind_speed = wind_speed
        self._location_name = location_name
        self._forecast_daily = forecast_daily
        self._forecast_hourly = forecast_hourly

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)"""
        return self._temperature

    @property
    def dew_point(self) -> float:
        """Dew Point (Celcius)"""
        return self._dew_point

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def cloud_cover(self) -> int:
        """Cloud Coverage."""
        return self._cloud_cover

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def humidity(self) -> int:
        """Humidity (%)."""
        return self._humidity

    @property
    def apparent_temperature(self) -> float:
        """Feels like temperature (Celcius)."""
        return self._apparent_temperature

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def precipitation_probability(self) -> int:
        """Posobility of Precipiation (%)."""
        return self._precipitation_probability

    @property
    def pressure(self) -> float:
        """Sea Level Pressure (MB)"""
        return self._pressure

    @property
    def solarradiation(self) -> float:
        """Solar Radiation (w/m2)"""
        return self._solarradiation

    @property
    def visibility(self) -> int:
        """Visibility (km)"""
        return self._visibility

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)"""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)"""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)"""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index"""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time"""
        return self._datetime

    @property
    def location_name(self) -> str:
        """Location name."""
        return str(self._location_name).capitalize()

    @property
    def forecast_daily(self) -> ForecastDailyData:
        """Forecast List"""
        return self._forecast_daily

    @forecast_daily.setter
    def forecast_daily(self, new_forecast):
        """Sets a new Value for forecast daily"""
        self._forecast_daily = new_forecast

    @property
    def forecast_hourly(self) -> ForecastHourlyData:
        """Forecast List"""
        return self._forecast_hourly

    @forecast_hourly.setter
    def forecast_hourly(self, new_forecast):
        """Sets a new Value for forecast hourly"""
        self._forecast_hourly = new_forecast


class ForecastDailyData:
    """Class to hold daily forecast data."""

    # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        temperature: float,
        temp_low: float,
        apparent_temperature: float,
        condition: str,
        icon: str,
        cloud_cover: int,
        dew_point: float,
        humidity: int,
        precipitation_probability: int,
        precipitation: float,
        pressure: float,
        wind_bearing: int,
        wind_speed: float,
        wind_gust: float,
        uv_index: int,
    ) -> None:
        """Constructor"""
        self._datetime = datetime
        self._temperature = temperature
        self._temp_low = temp_low
        self._apparent_temperature = apparent_temperature
        self._condition = condition
        self._cloud_cover = cloud_cover
        self._dew_point = dew_point
        self._humidity = humidity
        self._icon = icon
        self._precipitation_probability = precipitation_probability
        self._precipitation = precipitation
        self._pressure = pressure
        self._wind_bearing = wind_bearing
        self._wind_gust = wind_gust
        self._wind_speed = wind_speed
        self._uv_index = uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time"""
        return self._datetime

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)"""
        return self._temperature

    @property
    def temp_low(self) -> float:
        """Air temperature min during the day (Celcius)"""
        return self._temp_low

    @property
    def apparent_temperature(self) -> float:
        """Feels like temperature (Celcius)."""
        return self._apparent_temperature

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def cloud_cover(self) -> int:
        """Cloud Coverage."""
        return self._cloud_cover

    @property
    def dew_point(self) -> float:
        """Dew Point (Celcius)"""
        return self._dew_point

    @property
    def humidity(self) -> int:
        """Humidity (%)."""
        return self._humidity

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def precipitation_probability(self) -> int:
        """Posobility of Precipiation (%)."""
        return self._precipitation_probability

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def pressure(self) -> float:
        """Sea Level Pressure (MB)"""
        return self._pressure

    @property
    def uv_index(self) -> float:
        """UV Index"""
        return self._uv_index

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)"""
        return self._wind_bearing

    @property
    def wind_gust(self) -> float:
        """Wind Gust speed (m/s)"""
        return self._wind_gust

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)"""
        return self._wind_speed


class ForecastHourlyData:
    """Class to hold hourly forecast data."""

    # pylint: disable=R0913, R0902, R0914
    def __init__(
        self,
        datetime: datetime,
        temperature: float,
        apparent_temperature: float,
        condition: str,
        cloud_cover: int,
        icon: str,
        dew_point: float,
        humidity: int,
        precipitation: float,
        precipitation_probability: int,
        pressure: float,
        wind_bearing: float,
        wind_gust_speed: int,
        wind_speed: int,
        uv_index: float,
    ) -> None:
        """Constructor"""
        self._datetime = datetime
        self._temperature = temperature
        self._apparent_temperature = apparent_temperature
        self._condition = condition
        self._cloud_cover = cloud_cover
        self._icon = icon
        self._dew_point = dew_point
        self._humidity = humidity
        self._precipitation = precipitation
        self._precipitation_probability = precipitation_probability
        self._pressure = pressure
        self._wind_bearing = wind_bearing
        self._wind_gust_speed = wind_gust_speed
        self._wind_speed = wind_speed
        self._uv_index = uv_index

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)"""
        return self._temperature

    @property
    def condition(self) -> str:
        """Weather condition text."""
        return self._condition

    @property
    def cloud_cover(self) -> int:
        """Cloud Coverage."""
        return self._cloud_cover

    @property
    def dew_point(self) -> float:
        """Dew Point (Celcius)"""
        return self._dew_point

    @property
    def icon(self) -> str:
        """Weather condition symbol."""
        return self._icon

    @property
    def humidity(self) -> int:
        """Humidity (%)."""
        return self._humidity

    @property
    def apparent_temperature(self) -> float:
        """Feels like temperature (Celcius)."""
        return self._apparent_temperature

    @property
    def precipitation(self) -> float:
        """Precipitation (mm)."""
        return self._precipitation

    @property
    def precipitation_probability(self) -> int:
        """Posobility of Precipiation (%)."""
        return self._precipitation_probability

    @property
    def pressure(self) -> float:
        """Sea Level Pressure (MB)"""
        return self._pressure

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)"""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)"""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)"""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index"""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time"""
        return self._datetime

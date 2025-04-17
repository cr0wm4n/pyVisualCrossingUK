"""Holds the Data Classes for Visual Crossing Wrapper."""

from __future__ import annotations
from datetime import datetime


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
        solar_radiation: float,
        temperature: float,
        visibility: int,
        uv_index: int,
        wind_bearing: int,
        wind_gust_speed: float,
        wind_speed: float,
        location_name: str,
        description: str,
        datetimeepoch: int,
        snow: float,
        snow_depth: float,
        precipitation_type: str,
        solar_energy: float,
        severe_risk: float,
        sunrise: str,
        sunset: str,
        moonphase: float,
        
        forecast_daily: ForecastDailyData = None,
        forecast_hourly: ForecastHourlyData = None,
    ) -> None:
        """Dataset constructor."""
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
        self._solar_radiation = solar_radiation
        self._visibility = visibility
        self._temperature = temperature
        self._uv_index = uv_index
        self._wind_bearing = wind_bearing
        self._wind_gust_speed = wind_gust_speed
        self._wind_speed = wind_speed
        self._location_name = location_name
        self._description = description
        self._datetimeepoch = datetimeepoch
        self._snow = snow
        self._snow_depth = snow_depth
        self._precipitation_type = precipitation_type
        self._solar_energy = solar_energy
        self._severe_risk = severe_risk
        self._sunrise = sunrise
        self._sunset = sunset
        self._moonphase = moonphase
        self._forecast_daily = forecast_daily
        self._forecast_hourly = forecast_hourly

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
        return self._temperature

    @property
    def dew_point(self) -> float:
        """Dew Point (Celcius)."""
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
        """Sea Level Pressure (MB)."""
        return self._pressure

    @property
    def solar_radiation(self) -> float:
        """Solar Radiation (w/m2)."""
        return self._solar_radiation

    @property
    def visibility(self) -> int:
        """Visibility (km)."""
        return self._visibility

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)."""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index."""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def datetimeepoch(self) -> int:
        """ datetimeEpoch."""
        return self._datetimeepoch

    @property
    def snow(self) -> float:
        """Snow."""
        return self._snow

    @property
    def snow_depth(self) -> float:
        """Snow Depth."""
        return self._snow_depth

    @property
    def precipitation_type(self) -> str:
        """Precipitation Type text."""
        return self._precipitation_type

    @property
    def solar_energy(self) -> float:
        """Solar Energy."""
        return self._solar_energy

    @property
    def severe_risk(self) -> float:
        """Severe Weather Risk."""
        return self._severe_risk

    @property
    def sunrise(self) -> str:
        """Sunrise."""
        return self._sunrise

    @property
    def sunset(self) -> str:
        """Sunset."""
        return self._sunset
        
    @property
    def moonphase(self) -> float:
        """Moonphase."""
        return self._moonphase
        
    @property
    def location_name(self) -> str:
        """Location name."""
        return str(self._location_name).capitalize()

    @property
    def description(self) -> str:
        """Weather Description."""
        return self._description

    @property
    def update_time(self) -> datetime:
        """Last updated."""
        return datetime.now().isoformat()

    @property
    def forecast_daily(self) -> ForecastDailyData:
        """Forecast List."""
        return self._forecast_daily

    @forecast_daily.setter
    def forecast_daily(self, new_forecast):
        """Forecast daily new value."""
        self._forecast_daily = new_forecast

    @property
    def forecast_hourly(self) -> ForecastHourlyData:
        """Forecast List."""
        return self._forecast_hourly

    @forecast_hourly.setter
    def forecast_hourly(self, new_forecast):
        """Forecast hourly new value."""
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
        datetimeepoch: int,
        temp_high: float,
        apparent_temperature_high: float,
        apparent_temperature_low: float,
        precipitation_cover: float,
        precipitation_type: str,
        snow: float,
        snow_depth: float,
        visibility: float,
        solar_radiation: float,
        solar_energy: float,
        severe_risk: float,
        wind_speed_max: float,
        wind_speed_mean: float,
        wind_speed_min: float,
        sunrise: str,
        sunset: str,
        moonphase: float,
        description: str,
        
    ) -> None:
        """Dataset constructor."""
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
        self._datetimeepoch = datetimeepoch
        self._temp_high = temp_high
        self._apparent_temperature_high = apparent_temperature_high
        self._apparent_temperature_low = apparent_temperature_low
        self._precipitation_cover = precipitation_cover
        self._precipitation_type = precipitation_type
        self._snow = snow
        self._snow_depth = snow_depth
        self._visibility = visibility
        self._solar_radiation = solar_radiation
        self._solar_energy = solar_energy
        self._severe_risk = severe_risk
        self._wind_speed_max = wind_speed_max
        self._wind_speed_mean = wind_speed_mean
        self._wind_speed_min = wind_speed_min
        self._sunrise = sunrise
        self._sunset = sunset
        self._moonphase = moonphase
        self._description = description        

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
        return self._temperature

    @property
    def temp_low(self) -> float:
        """Air temperature min during the day (Celcius)."""
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
        """Dew Point (Celcius)."""
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
        """Sea Level Pressure (MB)."""
        return self._pressure

    @property
    def uv_index(self) -> float:
        """UV Index."""
        return self._uv_index

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_gust(self) -> float:
        """Wind Gust speed (m/s)."""
        return self._wind_gust

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def datetimeepoch(self) -> int:
        """datetime epoch."""
        return self._datetimeepoch

    @property
    def temp_high(self) -> float:
        """Air temperature max during the day (Celcius)."""
        return self._temp_high

    @property
    def apparent_temperature_high(self) -> float:
        """Feels like temperature high(Celcius)."""
        return self._apparent_temperature_high

    @property
    def apparent_temperature_low(self) -> float:
        """Feels like temperature low(Celcius)."""
        return self._apparent_temperature_low

    @property
    def precipitation_cover(self) -> float:
        """Precipitation cover."""
        return self._precipitation_cover

    @property
    def precipitation_type(self) -> str:
        """Precipitation type."""
        return self._precipitation_type

    @property
    def snow(self) -> float:
        """snow."""
        return self._snow

    @property
    def snow_depth(self) -> float:
        """snow depth."""
        return self._snow_depth

    @property
    def visibility(self) -> float:
        """visibility."""
        return self._visibility

    @property
    def solar_radiation(self) -> float:
        """solar_radiation."""
        return self._solar_radiation

    @property
    def solar_energy(self) -> float:
        """solar_energy."""
        return self._solar_energy
 
    @property
    def severe_risk(self) -> float:
        """severe risk."""
        return self._severe_risk

    @property
    def wind_speed_max(self) -> float:
        """Wind speed max (m/s)."""
        return self._wind_speed_max

    @property
    def wind_speed_mean(self) -> float:
        """Wind speed mean(m/s)."""
        return self._wind_speed_mean

    @property
    def wind_speed_min(self) -> float:
        """Wind speed min(m/s)."""
        return self._wind_speed_min

    @property
    def sunrise(self) -> str:
        """Sunrise."""
        return self._sunrise

    @property
    def sunset(self) -> str:
        """Sunset."""
        return self._sunset

    @property
    def moonphase(self) -> float:
        """Moon phase."""
        return self._moonphase

    @property
    def description(self) -> str:
        """Description."""
        return self._description
     
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
        datetimeepoch: int,
        snow: float,
        snow_depth: float,
        precipitation_type: str,
        visibility: float,
        solar_radiation: float,
        solar_energy: float,
        severe_risk: float,
    ) -> None:
        """Dataset constructor."""
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
        self._datetimeepoch = datetimeepoch
        self._snow = snow
        self._snow_depth = snow_depth
        self._precipitation_type = precipitation_type
        self._visibility = visibility
        self._solar_radiation = solar_radiation
        self._solar_energy = solar_energy
        self._severe_risk = severe_risk
        
    @property
    def temperature(self) -> float:
        """Air temperature (Celcius)."""
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
        """Dew Point (Celcius)."""
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
        """Sea Level Pressure (MB)."""
        return self._pressure

    @property
    def wind_bearing(self) -> float:
        """Wind bearing (degrees)."""
        return self._wind_bearing

    @property
    def wind_gust_speed(self) -> float:
        """Wind gust (m/s)."""
        return self._wind_gust_speed

    @property
    def wind_speed(self) -> float:
        """Wind speed (m/s)."""
        return self._wind_speed

    @property
    def uv_index(self) -> float:
        """UV Index."""
        return self._uv_index

    @property
    def datetime(self) -> datetime:
        """Valid time."""
        return self._datetime

    @property
    def datetimeepoch(self) -> int:
        """Datetime Epoch."""
        return self._datetimeepoch

    @property
    def snow(self) -> float:
        """Snow."""
        return self._snow

    @property
    def snow_depth(self) -> float:
        """Snow Depth."""
        return self._snow_depth

    @property
    def precipitation_type(self) -> str:
        """Precipitation Type."""
        return self._precipitation_type

    @property
    def visibility(self) -> float:
        """Visibility."""
        return self._visibility

    @property
    def solar_radiation(self) -> float:
        """Solar Radiation."""
        return self._solar_radiation

    @property
    def solar_energy(self) -> float:
        """Solar Energy."""
        return self._solar_energy

    @property
    def severe_risk(self) -> float:
        """Severe Risk."""
        return self._severe_risk


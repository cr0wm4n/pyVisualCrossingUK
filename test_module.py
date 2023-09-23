"""
This module is only used to run some realtime data tests
while developing the module.
Create a .env file and add:
API_KEY: Your API key from Visual Crossing
LATITUDE: The latitude you want to get data for
LONGITUDE: The longitude you want to get data for
"""
from __future__ import annotations

from dotenv import load_dotenv
import os
import logging

from pyVisualCrossing import (
    VisualCrossing,
    VisualCrossingUnauthorized,
    ForecastData,
    ForecastDailyData,
    ForecastHourlyData,
)

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Read Values from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
latitude = os.getenv("LATITUDE")
longitude = os.getenv("LONGITUDE")
data = None

# Attach to API and fetch data
vcapi = VisualCrossing(api_key, latitude, longitude, days=7)
try:
    data: ForecastData = vcapi.fetch_data()
except VisualCrossingUnauthorized as erru:
    print(erru)

if data is not None:
    print("***** CURRENT CONDITIONS *****")
    print("TEMPERATURE: ", data.temperature, " WIND GUST SPEED: ", data.wind_gust_speed)
    print("LOCATION: ", data.location_name)
    print(" ")
    print(" ")

    print("***** DAILY DATA *****")
    item: ForecastDailyData = None
    for item in data.forecast_daily:
        print(item.datetime, item.temperature, item.temp_low, item.icon, item.condition)

    print("***** HOURLY DATA *****")
    item_hour: ForecastHourlyData = None
    for item_hour in data.forecast_hourly:
        print(
            item_hour.datetime,
            item_hour.temperature,
            item_hour.apparent_temperature,
            item_hour.icon,
            item_hour.condition,
        )

# Python Wrapper for Visual Crossing Weather API

This Python Wrapper retrives data from the [Visual Crossing](https://www.visualcrossing.com/) API. Visual Crossing has an extensive Weather API for both historical and forecast weather data, and they have a Free Tier API Key which enables up to 1000 calls per day.

In order to get started you must create an Account with Visual Crossing and then create an API Key. You do this by accessing [this website](https://www.visualcrossing.com/weather-data-editions) and clicking on the **Free** plan. Then follow the instructions to create and account and store your key in a safe place.

## Usage

Install the module by using this command in a terminal: `pip install pyVisualCrossing`

And then see `test_module.py` and `async_test_module.py` in the `samples` directory for usage examples, both standard and async.

## Parameters

```python
# Initialise the module
vcapi = VisualCrossing(
    api_key,
    latitude,
    longitude,
    days=7,
    language="da"
)
````

| Parameter | Required | Default | Description |
| --------- | -------- | ------- | ----------- |
| `api_key` | Yes      | `None`  | This is the API Key you signed up for from Visual Crossing. See above for instructions |
| `latitude` | Yes     | `None`  | Latitude for the location position |
| `longitude` | Yes     | `None`  | Longitude for the location position |
| `days` | No     | `14`  | Numbers of days to retrieve forecast for. 14 days means today plus the next 14 days. On the Free plan, this is the maximum number of days |
| `language` | No     | `en`  | The language in which text strings should be returned. Se below for list of valid languages. |
| `session` | No     | `None`  | A session variable. Only used when using the async function. |



For an in-depth description of the Visual Crossing API, go [here](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)

## Languages
Available languages include: ar (Arabic), bg (Bulgiarian), cs (Czech), da (Danish), de (German), el (Greek Modern), en (English), es (Spanish), fa (Farsi), fi (Finnish), fr (French), he (Hebrew), hu, (Hungarian), it (Italian), ja (Japanese), ko (Korean), nl (Dutch), pl (Polish), pt (Portuguese), ru (Russian),, sr (Serbian), sv (Swedish), tr (Turkish), uk (Ukranian), vi (Vietnamese) and zh (Chinese).

## Icons
We use the Iconset *icons2*, which gives a more detailed description of the conditions.

| Icon id	            | Weather Conditions |
| --------------------  | ---------------------------- |
| snow	                | Amount of snow is greater than zero |
| snow-showers-day	    | Periods of snow during the day |
| snow-showers-night    | Periods of snow during the night |
| thunder-rain	        | Thunderstorms throughout the day or night |
| thunder-showers-day   | Possible thunderstorms throughout the day |
| thunder-showers-night | Possible thunderstorms throughout the night |
| rain                  | Amount of rainfall is greater than zero |
| showers-day           | Rain showers during the day |
| showers-night         | Rain showers during the night |
| fog                   | Visibility is low (lower than one kilometer or mile) |
| wind                  | Wind speed is high (greater than 30 kph or mph) |
| cloudy                | Cloud cover is greater than 90% cover |
| partly-cloudy-day     | Cloud cover is greater than 20% cover during day time. |
| partly-cloudy-night   | Cloud cover is greater than 20% cover during night time. |
| clear-day             | Cloud cover is less than 20% cover during day time |
| clear-night           | Cloud cover is less than 20% cover during night time |

## TODO

- Add all available items to the Data Structure
- Create `async_test_module.py` in the samples directory
- More detailed error handling.
"""
08_openmeteo_weather.py
----------------------
Fetches current weather from Open-Meteo API with error handling.
"""

import requests
from requests.exceptions import RequestException, Timeout, HTTPError

weather_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "current_weather": True
}

try:
    response = requests.get(weather_url, params=params, timeout=5)
    response.raise_for_status()
    weather_data = response.json()
    current_temp = weather_data.get('current_weather', {}).get('temperature')
    print(f'Successfully retrieved weather! Current Temperature: {current_temp}°C')
except Timeout:
    print('The request timed out. Please try again later.')
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except RequestException as err:
    print(f'An error occurred while making the request: {err}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')

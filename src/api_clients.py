"""This module holds the APIClient class."""
import requests

class APIClient:
    """Client class responsible for interacting with external APIs."""
    BASE_URL_COORDINATES = "https://nominatim.openstreetmap.org/search?"
    BASE_URL_WEATHER = "https://api.open-meteo.com/v1/forecast"

    @staticmethod
    def get_coordinates(city:str, country: str):
        """Fetch coordinates for a city."""
        params = {
        "city": city,
        "country": country,
        "format": "json"
        }
        # Nominatim API requires populated header
        headers = {
            "User-Agent": "WeatherlyApp/1.0 (vs@weatherly.com)"
        }
        try:
            response = requests.get(APIClient.BASE_URL_COORDINATES, params=params, headers=headers, timeout=10)
            response.raise_for_status() # 4xx for client errors or 5xx for server errors
            data = response.json()
            return data                 # Returns a list of dicts here
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception occurred: {err}")


    @staticmethod
    def get_weather(latitude:float, longitude:float, timezone:str, **weather_params):
        """Fetch weather data for the given coordinates."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
            **weather_params
        }
        try:
            response = requests.get(APIClient.BASE_URL_WEATHER, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data                 # Returns a dict here
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")

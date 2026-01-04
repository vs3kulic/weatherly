"""This file holds the definition of the Weather class."""
import requests


class Weather:
    """A class to represent the Weather object."""

    def __init__(self, latitude:float, longitude:float, timezone:str):
        self._latitude = latitude
        self._longitude = longitude
        self._timezone = timezone


    def fetch_weather(self):
        """Client for the Open-Meteo API."""
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
        "latitude": self._latitude,
        "longitude": self._longitude,
        "timezone": self._timezone,
        "current": "temperature_2m,wind_speed_10m"
        }
        # Call the Meteo API and parse response
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            temperature = data.get("current", {}).get("temperature_2m", None)
            wind_speed = data.get("current", {}).get("wind_speed_10m", None)
            return {
                "temperature": temperature,
                "wind_speed": wind_speed
            }
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")


    # TODO: Add a __str__ method for better representation
    # TODO: Add input validation in the constructor
    # TODO: Add properties for accessing coordinates
    # TODO: Consider adding a class method to create a Weather instance from a City

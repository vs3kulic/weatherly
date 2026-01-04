"""This file holds the definition of the Weather class."""
import requests


class Weather:
    """A class to represent the Weather object."""

    def __init__(self, latitude: float, longitude: float, timezone: str, 
                temperature: float = None, wind_speed: float = None, elevation: float = None):
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {latitude}")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude must be between -100 and 100, got {longitude}")
        if not isinstance(timezone, str) or not timezone.strip():
            raise ValueError("Timezone must be a non-empty string.")
        self._latitude = latitude
        self._longitude = longitude
        self._timezone = timezone
        # Calculated attributes (default=None)
        self._temperature = temperature
        self._wind_speed = wind_speed
        self._elevation = elevation


    def __str__(self):
        return (f"Location:             {self._latitude}, {self._longitude} ({self._timezone})\n"
                f"Temperature (in °C):  {self._temperature}\n"
                f"Wind speed (in km/h): {self._wind_speed}\n"
                f"Elevation:            {self._elevation}")


    @classmethod
    def from_coordinates(cls, latitude, longitude, timezone):
        """Create a Weather instance and fetch data."""
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
            "current": "temperature_2m,wind_speed_10m"
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            temperature = data.get("current", {}).get("temperature_2m", None)
            wind_speed = data.get("current", {}).get("wind_speed_10m", None)
            elevation = data.get("elevation", None)

            return Weather(latitude, longitude, timezone, temperature, wind_speed, elevation)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
        
        # Return a default Weather object if the API call fails
        return Weather(latitude, longitude, timezone)


    @property
    def temperature(self):
        """Get the current temperature"""
        if self._temperature is None:
            print("Warning: Temperature could not be fetched.")
        return self._temperature

    @property
    def wind_speed(self):
        """Get the current wind speed."""
        if self._wind_speed is None:
            print("Warning: Wind speed could not be fetched.")
        return self._wind_speed

    @property
    def elevation(self):
        """Get the elevation of the measurement."""
        if self._elevation is None:
            print("Warning: Elevation could not be fetched.")
        return self._elevation

    # TODO: Add input validation in the constructor


def main():
    lat_ = 48.21
    lon_ = 16.37
    tz_ = "CET"

    # Create Weather object using Class Factory Method
    w = Weather.from_coordinates(lat_, lon_, tz_)
    print(w.temperature)


if __name__ == "__main__":
    main()
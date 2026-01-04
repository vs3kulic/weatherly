"""This file holds the definition of the Weather class."""
from api_clients import APIClient


class Weather:
    """A class to represent the Weather object."""

    def __init__(self, latitude: float, longitude: float, timezone: str,
                temperature: float = None, wind_speed: float = None, elevation: float = None):
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {latitude}")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {longitude}")
        self._latitude = latitude
        self._longitude = longitude
        self._timezone = timezone
        # Store calculated attributes (default=None)
        self._temperature = temperature
        self._wind_speed = wind_speed
        self._elevation = elevation


    def __str__(self):
        return (f"Location:             {self._latitude}, {self._longitude}\n"
                f"Temperature (in °C):  {self._temperature}\n"
                f"Wind speed (in km/h): {self._wind_speed}\n"
                f"Elevation:            {self._elevation}")


    @classmethod
    def from_coordinates(cls, latitude, longitude, timezone=None):
        """Create a Weather instance."""
        # Validate latitude and longitude
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {latitude}")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {longitude}")

        # Explicit default assignment
        if timezone is None:
            timezone = "CET"

        # Call API Client class to get weather data
        weather_data = APIClient.get_weather(latitude, longitude)
        if not isinstance(weather_data, dict):
            raise ValueError("Invalid weather data received from APIClient.")

        # Parse the information from the response JSON
        temperature = weather_data.get("current", {}).get("temperature_2m", 0.0)
        wind_speed = weather_data.get("current", {}).get("wind_speed_10m", 0.0)
        elevation = weather_data.get("elevation", 0.0)

        # Create the weather object
        return Weather(latitude, longitude, timezone, temperature, wind_speed, elevation)


    @property
    def temperature(self):
        """Get the current temperature"""
        return self._temperature

    @property
    def wind_speed(self):
        """Get the current wind speed."""
        return self._wind_speed

    @property
    def elevation(self):
        """Get the elevation of the measurement."""
        return self._elevation


def main():
    # Hard-coded Latitude and Longitude values for Demo
    lat = 48.21
    lon = 16.37

    # Create Weather object using Class Factory Method
    w2 = Weather.from_coordinates(lat, lon)
    print(f"Temperature:    {w2.temperature}° Celsius\n"
          f"Wind speed:     {w2.wind_speed} km/h\n"
          f"Elevation:      {w2.elevation} m above sea-level")


if __name__ == "__main__":
    main()

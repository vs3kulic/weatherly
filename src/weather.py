"""This file holds the definition of the Weather class."""
from api_clients import APIClient


class Weather:
    """A class to represent the Weather object."""

    def __init__(self, city, country, temperature=None, wind_speed=None, elevation=None):
        self._city = city
        self._country = country
        # Store calculated attributes
        self._temperature = temperature
        self._wind_speed = wind_speed
        self._elevation = elevation


    def __str__(self):
        return (f"Location:             {self._city}, {self._country}\n"
                f"Temperature (in °C):  {self._temperature}\n"
                f"Wind speed (in km/h): {self._wind_speed}\n"
                f"Elevation:            {self._elevation}")

    
    @staticmethod
    def _get_coordinates(city, country):
        coordinates = APIClient.get_coordinates(city, country)
        if not coordinates or len(coordinates) == 0:
            raise ValueError(f"No coordinates found for {city}, {country}")
        latitude = float(coordinates[0].get("lat"))
        longitude = float(coordinates[0].get("lon"))
        return latitude, longitude

    @classmethod
    def for_city(cls, city, country, timezone=None):
        """Create a Weather instance for a city and country."""
        # Validate timezone (Explicit Default Assignment or Mutable Default Argument Guard)
        if timezone is None:
            timezone = "CET"
        
        # Get and validate coordinates
        latitude, longitude = cls._get_coordinates(city, country)
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {latitude}")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {longitude}")

        # Get weather data
        weather_data = APIClient.get_weather(latitude, longitude, timezone)
        if not isinstance(weather_data, dict):
            raise ValueError("Invalid weather data received from APIClient.")

        # Parse weather information
        temperature = weather_data.get("current", {}).get("temperature_2m", 0.0)
        wind_speed = weather_data.get("current", {}).get("wind_speed_10m", 0.0)
        elevation = weather_data.get("elevation", 0.0)

        # Create and return weather object
        return Weather(city, country, temperature, wind_speed, elevation)


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
    # Hard-coded city and country values for Demo
    city = "Vienna"
    country = "Austria"

    w2 = Weather.for_city(city, country)
    print(f"Temperature:    {w2.temperature}° Celsius\n"
          f"Wind speed:     {w2.wind_speed} km/h\n"
          f"Elevation:      {w2.elevation} m above sea-level")

if __name__ == "__main__":
    main()

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
    def _get_coordinates(city:str, country:str) -> tuple[float, float]:
        # Call Nominatim API via the API Client
        coordinates = APIClient.get_coordinates(city, country)

        # Validate the returned list[dict] object (from JSON)
        if not coordinates or len(coordinates) == 0:
            raise ValueError(f"No coordinates found for {city}, {country}")
        if not isinstance(coordinates, list):
            raise ValueError("Invalid coordinates received from APIClient.")

        # Parse the coordinates object for required values
        latitude = float(coordinates[0].get("lat"))
        longitude = float(coordinates[0].get("lon"))

        # Validate the received values
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude must be between -90 and 90, got {latitude}")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude must be between -180 and 180, got {longitude}")

        return latitude, longitude


    @staticmethod
    def _get_weather(latitude:float, longitude:float, timezone:str = None) -> tuple[float, float, float]:
        # Set explicit default value
        if timezone is None:
            timezone = "CET"

        # Call Meteo API via the API Client
        weather_data = APIClient.get_weather(latitude, longitude, timezone, hourly="temperature_2m", current="wind_speed_10m")

        # Validate the returned dict object (from JSON)
        if not weather_data or len(weather_data) == 0:
            raise ValueError("No weather data received from APIClient")
        if not isinstance(weather_data, dict):
            raise ValueError("Invalid weather data received from APIClient.")

        # Parse the weather_data object for required values
        hourly_temperatures = weather_data.get("hourly", {}).get("temperature_2m", 0.0)
        temperature = min(hourly_temperatures)
        wind_speed = weather_data.get("current", {}).get("wind_speed_10m", 0.0)
        elevation = weather_data.get("elevation", 0.0)

        return temperature, wind_speed, elevation


    @classmethod
    def for_city(cls, city, country):
        """Create a Weather instance for a city and country."""
        # Validate inputs
        if not city.strip() or not country.strip():
            raise ValueError("City and country must not be empty.")
        if not isinstance(city, str) or not isinstance(country, str):
            raise ValueError("City and country must be non-empty strings.")

        # Get coordinates
        latitude, longitude = cls._get_coordinates(city, country)

        # Get weather data from coordinates
        temperature, wind_speed, elevation = cls._get_weather(latitude, longitude)

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
    """THe main() function demonstrates the Weather class."""
    city = "Vienna"
    country = "Austria"

    w2 = Weather.for_city(city, country)
    print(f"Temperature:    {w2.temperature}° Celsius\n"
          f"Wind speed:     {w2.wind_speed} km/h\n"
          f"Elevation:      {w2.elevation} m above sea-level")

if __name__ == "__main__":
    main()

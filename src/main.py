import requests
from weather import Weather


def get_weather_data(latitude:float, longitude:float, timezone:str):
    """
    Client for the Open-Meteo API.
    
    Gets the temperature (in °C), elevation (in meters) and wind-speed (in km/h)
    for a given latitude, longitude and timezone.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        tz (str): Timezone of the location (e.g., "CET")
    Returns:
        dict: A dictionary containing temperature (float) and elevation (float)
    """
    # Construct the URL with parameters
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "current": "temperature_2m,wind_speed_10m"  # TODO: Hard-coded for now. Review other values
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


def get_city_coordinates(city:str, country: str):
    """Client for the Nominatim API.
    
    Gets the coordinates given a city name and country.
    
    Args:
        city (str): The city to look up.
        country (str): The country in which the city is located.
    Returns:
        dict (float): A dictionary with the latitude and longitude values.
    """
    # Construct URL with parameters
    url = "https://nominatim.openstreetmap.org/search?"
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
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        first_result = data[0]  # First entry in list of dicts (JSON)
        latitude = first_result.get("lat", None)
        longitude = first_result.get("lon", None)
        return {
            "latitude": latitude,
            "longitude": longitude
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception occurred: {err}")


def main():
    """Main function to demonstrate the weather data."""
    city_ = "Vienna"
    country_ = "Austria"
    lat_ = 48.21
    lon_ = 16.37
    tz_ = "CET"

    city = get_city_coordinates(city_, country_)
    weather = get_weather_data(lat_, lon_, tz_)

    if city:
        print(f"City:           {city_}, {country_}")
        print(f"Latitude:       {city["latitude"]}")
        print(f"Longitude:      {city["longitude"]}")
    else:
        print("Could not fetch city coordinates.")
        
    if weather:
        print(f"Temperature:    {weather["temperature"]}° Celsius.")
        print(f"Wind-speed:     {weather["wind_speed"]} km/h.")
    else:
        print("Could not fetch weather data.")

    w1 = Weather(lat_, lon_, tz_)
    print(w1)

if __name__ == "__main__":
    main()

import requests


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
        elevation = data.get("elevation", None)
        return {
            "temperature": temperature,
            "wind_speed": wind_speed,
            "elevation": elevation
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def main():
    """Main function to demonstrate the weather data."""
    latitude = 48.21
    longitude = 16.37
    timezone = "CET"

    temp = get_weather_data(latitude, longitude, timezone)

    if temp:
        print(f"Temperature in Vienna:      {temp["temperature"]}° Celsius.")
        print(f"The wind-speed is:          {temp["wind_speed"]} km/h.")
        print(f"Altitude above sea-level:   {temp["elevation"]} m")
    else:
        print("Could not fetch weather data.")


if __name__ == "__main__":
    main()

"""This is the main application module."""
from weather import Weather
import os
from glob import glob


def get_user_input():
    """Gets the city and country inputs from user."""
    city = input("\U0001F4CD Please choose a city: ").strip()
    country = input(f"\U0001F30D In which country is {city}: ").strip()
    return city, country


def display_weather(weather_obj):
    """Display weather information in a formatted way."""
    print("WEATHER REPORT")
    print("-" * 46)
    print(weather_obj)
    print("-" * 46)


def get_user_note():
    """Get the user note and save it to a file."""
    pass


def display_quote():
    """Retrieve a quote from a file and display it."""
    pass


def main():
    """Main application flow."""
    print("=" * 46)
    person1 = "Luka \U0001F917"
    print(f"🌤️  HELLO {person1.upper()}! WELCOME TO WEATHERLY 🌤️\n")  # Check Unicode character
    print("I'm your personal Weather Assistant!")
    print()
    city, country = get_user_input()
    print()
    print("OK! Fetching the data...")
    print()
    weather = Weather.for_city(city, country)
    display_weather(weather)
    # Get user note
    # Display quote


if __name__ == "__main__":
    main()

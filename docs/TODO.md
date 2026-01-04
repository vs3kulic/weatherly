# TODO

## Project Plan

### Step 1: Set Up the Project
- [x] Create project directory and virtual environment
- [x] Add a `README.md` file to describe the project
- [x] Install necessary libraries (`requests`, etc.)
- [ ] Write the project outline (describe the app's purpose and functionality)

### Step 2: Research and Understand APIs
- [ ] Research public weather forecast APIs (e.g., Open-Meteo)
- [ ] Read OpenStreetMap API (Nominatim) documentation
- [ ] Check API URLs and response structures (JSON)
- [ ] Learn how to perform HTTP requests using `requests`
- [ ] Learn how to parse JSON objects in Python

### Step 3: Implement Core Functionality
- [ ] Create a `models.py` file to store classes
- [ ] Create an `APIClient` class to handle API requests:
  - [ ] Fetch city coordinates from Nominatim
  - [ ] Fetch weather data from Open-Meteo
- [ ] Create a `City` class:
  - [ ] Store city name, country, latitude, and longitude
  - [ ] Use `APIClient` to fetch coordinates
- [ ] Create a `Weather` class:
  - [ ] Store weather data (temperature, wind speed, elevation)
  - [ ] Use `APIClient` to fetch weather data
  - [ ] Add a `from_coordinates` class method to create `Weather` objects with pre-fetched data

### Step 4: Add Functionality for Multiple Cities
- [ ] Allow the user to input multiple cities
- [ ] Create `City` objects for each city
- [ ] Use the `Weather` class to fetch weather data for each city
- [ ] Display weather data for all cities in a clean format

### Step 5: Add Extra Features
- [ ] Set up clothing tips based on temperature, wind, and rain
- [ ] Add a `.txt` file with motivational quotes to display in the app
- [ ] Allow the user to select a city from a predefined list

---

## Notes
- Keep the implementation simple and within the Python I curriculum at JKU.
- Focus on using basic Python concepts:
  - Classes and objects
  - HTTP requests with `requests`
  - JSON parsing
  - Error handling
- Avoid advanced topics like asynchronous programming or external frameworks.
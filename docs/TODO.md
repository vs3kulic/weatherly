# TODO

## Project Plan

### Step 1: Set up Project
- [x] Create project directory and virtual environment
- [x] Add a `README.md` file to describe the project
- [x] Install necessary libraries (`requests`, etc.)
- [x] Write the project outline (describe the app's purpose and functionality)

### Step 2: Research and understand APIs
- [x] Research public weather forecast APIs (Open-Meteo)
- [x] Read OpenStreetMap API (Nominatim) documentation
- [x] Check API URLs and response structures (JSON)
- [x] Learn how to perform HTTP requests using `requests`
- [x] Learn how to parse JSON objects in Python

### Step 3: Implement Core Functionality
- [x] Create `api_clients.py` file with `APIClient` class:
  - [x] Fetch city coordinates from Nominatim
  - [x] Fetch weather data from Open-Meteo
- [x] Create `weather.py` file with `Weather` class:
  - [x] Store weather data (temperature, wind speed, elevation)
  - [x] Use `APIClient` to fetch weather data
  - [x] Add `for_city` class method to create `Weather` objects from city/country
  - [x] Add proper validation and error handling

### Step 4: Refactor Main Application
- [ ] Refactor `main.py` to create interactive terminal application:
  - [ ] Prompt user for city and country input
  - [ ] Display weather information in clean format
  - [ ] Handle API errors gracefully with user-friendly messages
  - [ ] Add input validation for user entries

### Step 5: Add Note-Taking Feature
- [ ] Create user note functionality:
  - [ ] Prompt user to input weather observation notes
  - [ ] Create `notes.txt` file to store user notes with timestamps
  - [ ] Add function to append notes to the text file
  - [ ] Format notes with date, location, and user observation

### Step 6: Add Quote of the Day Feature
- [ ] Create quote system:
  - [ ] Create `quotes.txt` file with motivational/weather-related quotes
  - [ ] Add function to randomly select and display a quote
  - [ ] Display quote at the end of each weather session

### Step 7: Polish and Final Features 🎯
- [ ] Add error handling for network issues
- [ ] Add option to check weather for multiple cities in one session
- [ ] Add graceful exit options
- [ ] Test with various city/country combinations

---

## Notes
- Focus on creating a smooth user experience in the terminal
- Keep file I/O simple with basic text files

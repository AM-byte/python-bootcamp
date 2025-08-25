# Weather CLI App

A simple Python CLI app to fetch current weather data using the OpenWeather API.

## Features
- Get weather for any city via command line
- Displays:
  -  Temperature (Celsius)
  -  Humidity
  -  Weather description

## Setup Instructions

1. Clone the repo:
  ```bash
  git clone https://github.com/yourusername/weather-cli.git
  cd weather-cli
  ```

2. Create a .env file and add your API key:
  ```bash
  OPENWEATHER_API_KEY=your_api_key_here
  ```

3. Run the app
  ```bash
  python weather-app.py <city>
  ```
import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
  """
  Fetch weather for the given city and print it nicely.
  """
  url = "https://api.openweathermap.org/data/2.5/weather"
  
  params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # temperature in Celsius
  }
  
  response = requests.get(url, params=params)

  if response.status_code != 200:
    print(f"Error: Unable to fetch weather for '{city}'. Please check the city name.")
    return
  
  data = response.json()
  
  city_name = data["name"]
  temp = data["main"]["temp"]
  humidity = data["main"]["humidity"]
  description = data["weather"][0]["description"]
  
  print("="*40)
  print(f" Weather Report for {city_name}")
  print("="*40)
  print(f" Temperature: {temp} °C")
  print(f" Humidity: {humidity}%")
  print(f" Description: {description}")
  print("="*40)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python weather.py <city>")
  else:
    city = " ".join(sys.argv[1:])
    get_weather(city)
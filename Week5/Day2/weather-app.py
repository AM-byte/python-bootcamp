import requests
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd

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
    return None
  
  return response.json()

def get_weather_history(city):
  """
  Fetch 5-day forecast (3-hour intervals) for the given city.
  """
  url = "https://api.openweathermap.org/data/2.5/forecast"

  params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
  }

  response = requests.get(url, params=params)

  if response.status_code != 200:
    return None

  return response.json()

## Streamlit App

st.title("⛅ Weather Dashboard")
st.write("Enter a city below to get the current weather.")

city = st.text_input("City Name", "")

if city:
  data = get_weather(city)

  if data:
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    st.subheader(f"📍 Weather Report for {city_name}")
    st.metric("🌡️ Temperature (°C)", f"{temp:.1f}")
    st.metric("🌦️ Humidity (%)", f"{humidity}")
    st.write(f"☁️ Condition: **{description}**")

    # Weather forecast
    weather_forecast = get_weather_history(city)

    if weather_forecast:
      lst_forecast = weather_forecast["list"]
      df = pd.DataFrame({
        "Datetime": [item["dt_txt"] for item in lst_forecast],
        "Temperature (°C)": [item["main"]["temp"] for item in lst_forecast]
      })

      df["Datetime"] = pd.to_datetime(df["Datetime"])

      st.subheader(" 5-Day Temperature Forecast")
      st.line_chart(df.set_index("Datetime")["Temperature (°C)"])
    else:
      st.warning(" Could not fetch forecast data.")
  else:
    st.error(f" Could not fetch weather for `{city}`. Please try again.")
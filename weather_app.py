import streamlit as st
import requests

st.title("🌤️ Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo = requests.get(geo_url).json()

        if "results" in geo:
            lat = geo["results"][0]["latitude"]
            lon = geo["results"][0]["longitude"]

            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?"
                f"latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather = requests.get(weather_url).json()

            temp = weather["current_weather"]["temperature"]
            wind = weather["current_weather"]["windspeed"]

            st.success(f"Weather in {city}")
            st.write(f"🌡️ Temperature: {temp} °C")
            st.write(f"💨 Wind Speed: {wind} km/h")
        else:
            st.error("City not found")

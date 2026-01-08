import streamlit as st
import requests

API_KEY = "e8c80fd90275533a695cf079cc1ac75b"

st.title("🌤 Weather App")

city = st.selectbox("Select City", ["Pune", "Mumbai", "Delhi","Nagpur","Bangalore","Chennai","kolkata"])

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        st.success(f"📍 City: {city}")
        st.write(f"🌡 Temperature: {temp} °C")
        st.write(f"💧 Humidity: {humidity} %")
        st.write(f"☁ Weather: {condition}")
    else:
        st.error("City not found ❌")


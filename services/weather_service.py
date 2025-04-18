import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_coordinates(city_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "weather-app-flask"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if not data:
            return None, "Ciudad no encontrada"
        
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return (lat, lon), None
    
    except Exception as e:
        return None, f"Error al buscar coordenadas: {e}"

def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        #print(data, file=sys.stderr)
        weather_info = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"]
        }
        return weather_info, None
    
    except Exception as e:
        return None, f"Error al consultar el clima: {e}"

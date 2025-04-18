import requests
import os
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
        weather_info = {
            "city": data["name"],
            "temp": round(data["main"]["temp"], 1),
            "description": data["weather"][0]["description"]
        }
        return weather_info, None
    
    except Exception as e:
        return None, f"Error al consultar el clima: {e}"

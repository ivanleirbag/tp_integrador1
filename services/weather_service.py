import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_coordinates(city_name):
    """
    @brief Retrieves the geographic coordinates of a given city using the Nominatim API.

    @param city_name The name of the city to search for.

    @return A tuple depending on:
            Success: ((latitude, longitude), None)
            Failure: (None, error message as a string)
    """

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
    """
    @brief Retrieves current weather information for a given coordinate
            using the OpenWeatherMap API.

    @param lat Latitude.
    @param lon Longitude.

    @return A tuple depending on:
            Success: (dictionary containing weather data, None)
            Failure: (None, error message as a string)
    """

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
            "temp": round(data["main"]["temp"]),  
            "description": data["weather"][0]["description"].capitalize(),
            "feels_like": round(data["main"]["feels_like"]),
            "temp_min": round(data["main"]["temp_min"]),
            "temp_max": round(data["main"]["temp_max"]),
            "humidity": data["main"]["humidity"],
            "icon": data["weather"][0]["icon"]  
        }
        return weather_info, None
    
    except Exception as e:
        return None, f"Error al consultar el clima: {e}"

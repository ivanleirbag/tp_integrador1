from flask import Blueprint, render_template, request
from services.weather_service import get_coordinates, get_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city_name = request.form.get("city")
        
        if not city_name:
            return render_template("weather_templates.html", error="Debe ingresar una ciudad")

        coords, coord_error = get_coordinates(city_name)
        if coord_error:
            return render_template("weather_templates.html", error=coord_error)

        lat, lon = coords
        weather_data, weather_error = get_weather(lat, lon)

        if weather_error:
            return render_template("weather_templates.html", error=weather_error)

        return render_template("weather_templates.html", weather=weather_data)

    return render_template("weather_templates.html")

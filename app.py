from flask import Flask, render_template
from routes.main_routes import main_bp
from routes.number_routes import number_bp
from routes.weather_routes import weather_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(weather_bp, url_prefix="/weather")
app.register_blueprint(number_bp, url_prefix='/number')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_templates.html'), 404
    
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500_templates.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

# NumberC.py
from flask import Blueprint, render_template, request
from zeep import Client

number_bp = Blueprint('number_bp', __name__)

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')

@number_bp.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        number = request.form.get('number')
        if number.isdigit():
            result = client.service.NumberToWords(ubiNum=int(number))
        else:
            result = "Por favor, ingresa un número válido."
    return render_template('index.html', result=result)

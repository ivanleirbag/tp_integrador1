from flask import Flask, render_template, request
from zeep import Client

app = Flask(__name__)

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        number = request.form.get('number')
        if number.isdigit():
            result = client.service.NumberToWords(ubiNum=int(number))
        else:
            result = "Por favor, ingresa un número válido."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

from zeep import Client

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')

def convert_number_to_words(number):
    if number.isdigit():
        return client.service.NumberToWords(ubiNum=int(number))
    return "Por favor, ingresa un número válido."

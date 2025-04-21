from zeep import Client

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')

def convert_number_to_words(number):
    """
    @brief Converts a numeric string into its word representation using the NumberConversion SOAP service.

    @param number A string representing the number to be converted.

    @return A string depending on: 
              Valid input: The number in words.
              Invalid input: an error message.
    """

    if number.isdigit():
        return client.service.NumberToWords(ubiNum=int(number))
    return "Por favor, ingresa un número válido."

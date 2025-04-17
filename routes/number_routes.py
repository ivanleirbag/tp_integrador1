from flask import Blueprint, render_template, request
from services.number_service import convert_number_to_words

number_bp = Blueprint('number', __name__)

@number_bp.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        number = request.form.get('number')
        result = convert_number_to_words(number)
    return render_template('number_templates.html', result=result)

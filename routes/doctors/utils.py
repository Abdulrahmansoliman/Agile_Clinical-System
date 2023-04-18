from flask import abort, jsonify
from datetime import *

def validate_doctor_id(doctor_id):
    if doctor_id is None:
        abort(400, 'No doctor with the id provided')
    
    return jsonify({
        'success': True,
    })


def date_handler(data):    
    birth_date_str = data['birth_date']
    birth_date_obj = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
    
    return birth_date_obj
from flask import abort, jsonify
from datetime import *
from models.users.doctors import Doctor

def validate_doctor_id(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor is None or doctor.is_deleted == True:
        abort(400, 'No doctor with the id provided')
    
    return jsonify({
        'success': True,
    })


def date_handler(data):    
    birth_date_str = data['birth_date']
    birth_date_obj = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
    
    return birth_date_obj
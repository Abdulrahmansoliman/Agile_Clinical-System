from flask import (Blueprint,jsonify)
import sys
from datetime import *

from models.models import Doctor
from request_errors import requires_body

from routes.doctors.utils import validate_doctor_id, date_handler

doctors_blueprint = Blueprint('doctors', __name__)

@doctors_blueprint.route('/', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify({
        'success': True,
        'data': [d.format() for d in doctors]
    }), 200

@doctors_blueprint.route('/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    
    validate_doctor_id(doctor_id)
    doctor = Doctor.query.get(doctor_id)
    
    return jsonify({
        "success": True,
        "doctor": doctor.format()
    }), 200

@doctors_blueprint.route('/', methods=['POST'])
@requires_body("[username] [password] [email] [first_name] [last_name] [birth_date] [phone_number] [specialization]")
def create_doctor(data):
    
    birth_date_obj = date_handler(data)

    doctor_data = {
        "username": data['username'],
        "password": data['password'],
        "email": data['email'],
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "birth_date": birth_date_obj,
        "phone_number": data['phone_number'],
        "specialization": data['specialization']
    }
    
    doctor = Doctor(**doctor_data)
    doctor.insert()
    
    return jsonify({
        "success": True,
        "doctor": doctor.format()
    }), 201
<<<<<<< HEAD


@doctors_blueprint.route('/<int:doctor_id>', methods=['PATCH'])
@requires_body("[username] [password] [email] [first_name] [last_name] [birth_date] [phone_number] [specialization]")
def update_doctor(data, doctor_id):
    
    validate_doctor_id(doctor_id)
    doctor = Doctor.query.get(doctor_id)
    

    doctor.username = data['username']

    doctor.password = data['password']

    doctor.email = data['email']
    doctor.first_name = data['first_name']

    doctor.last_name = data['last_name']

    doctor.birth_date = date_handler(data)

    doctor.phone_number = data['phone_number']
    doctor.specialization = data['specialization']
    
    doctor.update()
    
    return jsonify({
        "success": True,
        "doctor": doctor.format()
    }), 200
 
 
=======
>>>>>>> 8b8bf7acea74195ecfcc4d8d8410ece1badf4943

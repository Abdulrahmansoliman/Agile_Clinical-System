from flask import (Blueprint,jsonify)
import sys
from models.models import Doctor

from routes.doctors.utils import validate_doctor_id

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

from models.patients.patients import Patient
from models.users.users import doctor_patient_association
from flask import (Blueprint, jsonify, request)
from routes.patients.utils import validate_patient_id
from request_errors import requires_body
from routes.doctors.utils import date_handler

patients_blueprint = Blueprint('patients', __name__)


@patients_blueprint.route('/', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify({
        'success': True,
        'data': [p.format() for p in patients],
        'number_of_patients': len(patients)
    }), 200


@patients_blueprint.route('/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    validate_patient_id(patient_id)

    patient = Patient.query.get(patient_id)
    return jsonify({
        'success': True,
        'data': patient.format()
    }), 200


@patients_blueprint.route('/', methods=['POST'])
@requires_body("[first_name] [last_name] [birth_date] [phone_number] [email]")
def add_patient(data):
    birth_date_obj = date_handler(data)

    patient_data = {
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "birth_date": birth_date_obj,
        "phone_number": data['phone_number'],
        "email": data['email']
    }

    patient = Patient(**patient_data)
    patient.insert()

    return jsonify({
        "success": True,
        "patient": patient.format()
    }), 201


@patients_blueprint.route('/<int:patient_id>', methods=['PATCH'])
@requires_body("[first_name] [last_name] [birth_date] [phone_number] [email]")
def edit_patient(data, patient_id):
    validate_patient_id(patient_id)

    birth_date_obj = date_handler(data)
    patient = Patient.query.get(patient_id)

    patient.first_name = data['first_name']
    patient.last_name = data['last_name']
    patient.birth_date = birth_date_obj
    patient.phone_number = data['phone_number']
    patient.email = data['email']

    patient.update()

    return jsonify({
        "success": True,
        "patient": patient.format()
    }), 200


@patients_blueprint.route('/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    validate_patient_id(patient_id)

    patient = Patient.query.get(patient_id)
    patient.delete()

    return jsonify({
        "success": True,
        "id_deleted": patient_id
    }), 200

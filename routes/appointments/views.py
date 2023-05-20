from flask import (Blueprint, abort, jsonify)
from models.appointments.appointments import Appointment
from routes.appointments.utils import validate_appointment_id
from request_errors import requires_body
from routes.appointments.utils import date_handler

appointments_blueprint = Blueprint('appointments', __name__)


@appointments_blueprint.route('/', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.filter_by(is_deleted=False).all()
    return jsonify({
        'success': True,
        'data': [a.format() for a in appointments]
    }), 200


@appointments_blueprint.route('/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    validate_appointment_id(appointment_id)
    appointment = Appointment.query.get(appointment_id)
    return jsonify({
        'success': True,
        'data': appointment.format()
    }), 200


@appointments_blueprint.route('/', methods=['POST'])
@requires_body("[patient_id] [doctor_id] [secretary_id] [start_time] [notes]")
def add_appointment(data):
    appointment_date_obj = date_handler(data)
    appointment_data = {
        "patient_id": data['patient_id'],
        "doctor_id": data['doctor_id'],
        "secretary_id": data['secretary_id'],
        "start_time": appointment_date_obj,
        "notes": data['notes']
    }
    print(appointment_data)

    appointment = Appointment(**appointment_data)
    appointment.insert()

    return jsonify({
        "success": True,
        "data": appointment.format()
    }), 201


@appointments_blueprint.route('/<int:appointment_id>', methods=['PATCH'])
@requires_body("[patient_id] [doctor_id] [secretary_id] [start_time] [notes]")
def edit_appointment(data, appointment_id):
    validate_appointment_id(appointment_id)

    appointment_date_obj = date_handler(data)
    appointment = Appointment.query.get(appointment_id)

    appointment.patient_id = data['patient_id']
    appointment.doctor_id = data['doctor_id']
    appointment.secretary_id = data['secretary_id']
    appointment.start_time = appointment_date_obj
    appointment.notes = data['notes']

    appointment.update()

    return jsonify({
        "success": True,
        "appointment": appointment.format()
    }), 200


@appointments_blueprint.route('/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    validate_appointment_id(appointment_id)
    appointment = Appointment.query.get(appointment_id)
    appointment.delete()
    return jsonify({
        "success": True,
        "appointment_id_deleted": appointment_id
    }), 200

from flask import (Blueprint, abort, jsonify)
from models.appointments.appointments import Appointment
from routes.appointments.utils import validate_appointment_id

appointments_blueprint = Blueprint('appointments', __name__)

@appointments_blueprint.route('/', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
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
    
    
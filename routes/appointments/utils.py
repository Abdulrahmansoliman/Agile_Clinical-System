from dateutil import parser
from flask import abort, jsonify
from models.appointments.appointments import Appointment
from datetime import *


def validate_appointment_id(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        error_message = "No appointment with id {} found".format(
            appointment_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))


def date_handler(data):
    birth_date_str = data['start_time']
   # birth_date_obj = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
    birth_date_obj = parser.parse(birth_date_str)
    return birth_date_obj

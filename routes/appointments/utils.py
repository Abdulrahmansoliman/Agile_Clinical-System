from flask import abort, jsonify
from models.appointments.appointments import Appointment

def validate_appointment_id(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment is None:
        error_message = "No appointment with id {} found".format(appointment_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))
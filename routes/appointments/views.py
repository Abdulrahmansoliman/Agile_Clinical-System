from flask import (Blueprint, abort, jsonify)
from models.appointments.appointments import Appointment

appointments_blueprint = Blueprint('appointments', __name__)

@appointments_blueprint.route('/', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify({
        'success': True,
        'data': [a.format() for a in appointments]
    }), 200


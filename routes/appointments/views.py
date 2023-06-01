from flask import (Blueprint, abort, jsonify,request)
from models.appointments.appointments import Appointment
from datetime import *  
from request_errors import requires_body
from routes.appointments.utils import date_handler
from routes.RouteFactory import RouteFactory


appointments_blueprint = Blueprint('appointments', __name__)
appointments_factory = RouteFactory(appointments_blueprint)

appointments_factory.generate_get_all_route(Appointment)
appointments_factory.get_one_route(Appointment)
appointments_factory.delete_one_route(Appointment)

@appointments_blueprint.route('/', methods=['POST'])
@requires_body("[patient_id] [doctor_id] [secretary_id] [start_time] [notes]")
def add_appointment(data):
    data['start_time'] = datetime.strptime(data['start_time'], '%Y-%m-%d')
    create = appointments_factory.create_one_route(Appointment)
    return create(data)
    

@appointments_blueprint.route('/<int:appointment_id>', methods=['PATCH'])
@requires_body("[patient_id] [doctor_id] [secretary_id] [start_time] [notes]")
def update_appointment(data, appointment_id):
    data['start_time'] = datetime.strptime(data['start_time'], '%Y-%m-%d')
    update = appointments_factory.update_one_route(Appointment,appointment_id)
    return update(data)

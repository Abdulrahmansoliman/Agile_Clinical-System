from models.records.records import Record
from flask import Blueprint, jsonify, abort
from request_errors import requires_body
from routes.records.utils import validate_record_id
from routes.records.utils import date_handler

records_blueprint = Blueprint('records', __name__)

@records_blueprint.route('/', methods=['GET'])
def get_records():
    records = Record.query.all()
    return jsonify({
        'success': True,
        'data': [r.format() for r in records]
    }), 200
 

@records_blueprint.route('/<int:record_id>', methods=['GET'])
def get_record(record_id):
    validate_record_id(record_id)
    record = Record.query.get(record_id)
    return jsonify({
        'success': True,
        'data': record.format()
    }), 200


@records_blueprint.route('/', methods=['POST'])
@requires_body("[date] [marital_status] [notes] [doctor_id] [patient_profile_id]")
def add_record(data):
    date_obj = date_handler(data)
    
    record_data = {
        "date": date_obj,
        "marital_status": data['marital_status'],
        "notes": data['notes'],
        "doctor_id": data['doctor_id'],
        "patient_profile_id": data['patient_profile_id']
    }
    
    record = Record(**record_data)
    record.insert()
    
    return jsonify({
        'success': True,
        'data': record.format()
    }), 201    
    

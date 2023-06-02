from models.records.records import Record
from models.records.reports import Report
from flask import Blueprint, jsonify, abort
from request_errors import requires_body
from routes.records.utils import *
from models.records.reportentities import ReportEntity
from models.init import *

records_blueprint = Blueprint('records', __name__)

@records_blueprint.route('/', methods=['GET'])
def get_records():
    records = Record.query.filter_by(is_deleted=False).all()
    return jsonify({
        'success': True,
        'data': [r.format() for r in records],
        'secondry data': [x.format() for x in records]
    }), 200
 

@records_blueprint.route('/<int:record_id>', methods=['GET'])
def get_record(record_id):
    validate_record_id(record_id)
    record = Record.query.get(record_id)
    return jsonify({
        'success': True,
        'data': record.format()
    }), 200

@records_blueprint.route('/<int:record_id>/reports', methods=['GET'])
def get_record_reports(record_id):
    validate_record_id(record_id)
    record = Record.query.get(record_id)
    return jsonify({
        'success': True,
        'data': record.get_reports_entities()
    }), 200

@records_blueprint.route('/<int:record_id>/reports/<int:entity_id>', methods=['GET'])
def get_record_report(record_id, entity_id):
    validate_record_id(record_id)
    report_of_entity = Report.query.filter_by(record_id=record_id, report_entity_id=entity_id).all()
    return jsonify({
        'success': True,
        'data': [r.format() for r in report_of_entity]
    }), 200

@records_blueprint.route('/', methods=['POST'])
@requires_body("[date] [marital_status] [notes] [doctor_id] [patient_profile_id] [reports]")
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
    
    for report in data['reports']:
        add_report(report, record.id)

    return jsonify({
        'success': True,
        'data': record.format()
    }), 201
    



@records_blueprint.route('/<int:record_id>', methods=['PATCH'])
@requires_body("[date] [marital_status] [notes] [doctor_id] [patient_profile_id] [reports]")
def edit_record(data,record_id):
    validate_record_id(record_id)
    date_obj = date_handler(data)
    
    record = Record.query.get(record_id)
    
    record.date = date_obj
    record.marital_status = data['marital_status']
    record.notes = data['notes']
    record.doctor_id = data['doctor_id']
    record.patient_profile_id = data['patient_profile_id']
    record.update()

    new_reports_ids = [report['report_id'] for report in data['reports']]

    # delete old reports
    for reports in record.reports:
        if reports.report_id not in new_reports_ids:
            reports.delete()


    for report_values in data['reports']['values']:
        old_report = ReportValue.query.get(report_values['id']).all()
        update_report(old_report, report_values)
    
    return jsonify({
        "sucess": True,
        "data": record.format()
    }), 200
    
def update_report(old_report, report):
    for value in report['values']:
        old_value = ReportValue.query.get(old_report['id'])
        old_value.value = value['value']
        

    

@records_blueprint.route('/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    validate_record_id(record_id)
    record = Record.query.get(record_id)
    record.delete()
    return jsonify({    
        "success": True,
        "id_deleted": record_id
    }), 200
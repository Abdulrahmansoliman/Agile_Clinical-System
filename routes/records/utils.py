from datetime import datetime
from flask import abort, jsonify
from models.records.records import Record
from models.records.reports import Report
from models.init import *

def validate_record_id(record_id):
    record = Record.query.get(record_id)
    if record is None or record.is_deleted == True:
        error_message = "No record with id {} found".format(record_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))

def validate_report_id(report_id):
    report = Report.query.get(report_id)
    if report is None or report.is_deleted == True:
        error_message = "No report with id {} found".format(report_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))

def validate_report_entity_id(report_entity_id):
    report_entity = ReportEntity.query.get(report_entity_id)
    if report_entity is None or report_entity.is_deleted == True:
        error_message = "No report entity with id {} found".format(report_entity_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))

def validate_report_attribute_id(report_attribute_id):
    report_attribute = ReportAttribute.query.get(report_attribute_id)
    if report_attribute is None or report_attribute.is_deleted == True:
        error_message = "No report attribute with id {} found".format(report_attribute_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))


def date_handler(data):
    date_obj = data ['date']
    date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()
    return date_obj
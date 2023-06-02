from flask import Blueprint, jsonify, abort
from request_errors import requires_body
from models.init import *
from routes.records.utils import validate_report_id, add_report

reports_blueprint = Blueprint('reports', __name__)

@reports_blueprint.route('/', methods=['GET'])
def get_reports():
    # Return a list of all reports
    reports = Report.query.all()
    formatted_reports = [report.format() for report in reports]
    return jsonify({
        'success': True,
        'data': formatted_reports
    }), 200


@reports_blueprint.route('/', methods=['POST'])
@requires_body("[record_id] [report_entity_id] [values]")
def add_report_route(data):
    report = add_report(data)
    return jsonify({
        "sucess": True,
        "data": report.format()
    }), 200


@reports_blueprint.route('/entities', methods=['GET'])
def get_entities():
    entities = ReportEntity.query.all()
    return jsonify({
        'success': True,
        'data': [e.format_with_attributes() for e in entities]
    }), 200


@reports_blueprint.route('/entities', methods=['POST'])
@requires_body("[name] [attributes]")
def add_entity(data):
    entity_data = {
        "name": data['name']
    }
    entity = ReportEntity(**entity_data)
    entity.insert()
    for attribute in data['attributes']:
        attribute_id = attribute['id']
        attribute = ReportAttribute.query.get(attribute_id)
        entity.attributes.append(attribute)
        
    return jsonify({
        'success': True,
        'data': entity.format_with_attributes()
    }), 201


@reports_blueprint.route('/attributes', methods=['POST'])
@requires_body("[name] [type]")
def add_attribute(data):
    attribute_data = {
        "name": data['name'],
        "type": data['type']
    }
    attribute = ReportAttribute(**attribute_data)
    attribute.insert()
    return jsonify({
        'success': True,
        'data': attribute.format()
    }), 201

@reports_blueprint.route('/attributes', methods=['GET'])
def get_attributes():
    attributes = ReportAttribute.query.all()
    return jsonify({
        'success': True,
        'data': [a.format() for a in attributes]
    }), 200

@reports_blueprint.route('/<int:report_id>', methods=['GET'])
def get_report(report_id):
    validate_report_id(report_id)
    report = Report.query.get(report_id)
    return jsonify({
        'success': True,
        'data': report.format()
    }), 200
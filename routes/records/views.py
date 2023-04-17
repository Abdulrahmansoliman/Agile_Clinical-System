from models.records.records import Record
from flask import Blueprint, jsonify, abort
from request_errors import requires_body

records_blueprint = Blueprint('records', __name__)

@records_blueprint.route('/', methods=['GET'])
def get_records():
    records = Record.query.all()
    return jsonify({
        'success': True,
        'data': [r.format() for r in records]
    }), 200
from flask import abort, jsonify
from models.records.records import Record

def validate_record_id(record_id):
    record = Record.query.get(record_id)
    if record is None:
        error_message = "No record with id {} found".format(record_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))
from datetime import datetime
from flask import abort, jsonify
from models.records.records import Record

def validate_record_id(record_id):
    record = Record.query.get(record_id)
    if record is None or record.is_deleted == True:
        error_message = "No record with id {} found".format(record_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))
        
def date_handler(data):
    date_obj = data ['date']
    date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()
    return date_obj
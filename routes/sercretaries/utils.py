from models.users.secretaries import Secretary

from request_errors import requires_body
from flask import (Blueprint,jsonify,abort)

def validate_secretary_id(secretary_id):
    secretary = Secretary.query.get(secretary_id)
    if secretary is None or secretary.is_deleted == True:
        error_message = "No secretary with id {} found".format(secretary_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))
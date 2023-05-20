from models.init import *
from flask import (Blueprint, jsonify, request)
from routes.patients.utils import validate_patient_id
from request_errors import requires_body
from routes.doctors.utils import date_handler

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['POST'])
@requires_body("[email] [password]")
def login(data):
    email = data['email']
    password = data['password']
    
    user = User.query.filter_by(email=email).first()
    usertype_id = user.usertypeid
    
    if user is None or not user.check_password(password):
        return jsonify({
            'success': False,
            'message': 'Invalid email or password'
        }), 401
    return jsonify({
        'success': True,
        'message': 'Logged in successfully',
        'usertype_id': usertype_id,
    }), 200



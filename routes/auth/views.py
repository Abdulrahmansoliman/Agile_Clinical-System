from models.init import *
from flask import (Blueprint, jsonify, request)
from routes.patients.utils import validate_patient_id
from request_errors import requires_body
from routes.auth.LoginFactory import LoginFactory

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['POST'])
@requires_body("[login_type] [email] [username] [password]")
def login(data):
    
    login_type = data['login_type']
    password = data['password']
    
    conflict_result = LoginFactory.check_conflicting_login_info(login_type, data)
    if conflict_result:
        return conflict_result
    
    login_strategy = LoginFactory.create_login_strategy(login_type)
    return login_strategy.login(data)


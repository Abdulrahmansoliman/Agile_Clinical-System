from models.users.secretaries import Secretary
from request_errors import requires_body
from routes.sercretaries.utils import validate_secretary_id
from flask import (Blueprint,jsonify)
from routes.doctors.utils import date_handler
from routes.RouteFactory import RouteFactory

secretaries_blueprint = Blueprint('secretaries', __name__)
secretaries_factory = RouteFactory(secretaries_blueprint)

secretaries_factory.generate_get_all_route(Secretary)
secretaries_factory.get_one_route(Secretary)
secretaries_factory.delete_one_route(Secretary)
    

    

@secretaries_blueprint.route('/', methods=['POST'])
@requires_body("[username] [password] [email] [first_name] [last_name] [birth_date] [phone_number]")
def create_secretary(data):
    birth_date_obj = date_handler(data)
    
    secretary_data = {
        "username": data['username'],
        "password": data['password'],
        "email": data['email'],
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "birth_date": birth_date_obj,
        "phone_number": data['phone_number']
    }
    
    secretary = Secretary(**secretary_data)
    secretary.insert()
    
    return jsonify({
        "success": True,
        "secretary": secretary.format()
    }), 201

@secretaries_blueprint.route('/<int:secretary_id>', methods=['PATCH'])
@requires_body("[username] [password] [email] [first_name] [last_name] [birth_date] [phone_number]")
def edit_secretary(data, secretary_id):
    validate_secretary_id(secretary_id)
    
    birth_date_obj = date_handler(data)
    secretary = Secretary.query.get(secretary_id)
    
    secretary.username = data['username']
    secretary.password = data['password']
    secretary.email = data['email']
    secretary.first_name = data['first_name']
    secretary.last_name = data['last_name']
    secretary.birth_date = birth_date_obj
    secretary.phone_numebr = data['phone_number']
    
    secretary.update()
    
    return jsonify({
        "success": True,
        "secretary": secretary.format()
    }), 200
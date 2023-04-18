from models.users.secretaries import Secretary
from request_errors import requires_body
from routes.sercretaries.utils import valiidate_secretary_id
from flask import (Blueprint,jsonify)
from routes.doctors.utils import date_handler

secretaries_blueprint = Blueprint('secretaries', __name__)


@secretaries_blueprint.route('/', methods=['GET'])
def get_secretaries():
    secretaries = Secretary.query.all()
    return jsonify({
        'success': True,
        'data': [s.format() for s in secretaries]
    }), 200
    

@secretaries_blueprint.route('/<int:secretary_id>', methods=['GET'])
def get_secretary(secretary_id):
    valiidate_secretary_id(secretary_id)
    secretary = Secretary.query.get(secretary_id)
    return jsonify({
        'success': True,
        'data': secretary.format()
    }), 200    
    

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
    valiidate_secretary_id(secretary_id)
    
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


@secretaries_blueprint.route('/<int:secretary_id>', methods=['DELETE'])
def delete_secretary(secretary_id):
    valiidate_secretary_id(secretary_id)
    
    secretary = Secretary.query.get(secretary_id)
    secretary.delete()
    
    return jsonify({
        "success": True,
        "deleted_id": secretary_id
    }), 200    
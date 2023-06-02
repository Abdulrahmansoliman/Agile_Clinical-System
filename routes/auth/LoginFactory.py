from models.init import *
from flask import  jsonify
from request_errors import requires_body
from routes.doctors.utils import date_handler


class LoginFactory:
    @staticmethod
    def create_login_strategy(login_type):
        if login_type == 'email':
            return EmailLoginStrategy()
        elif login_type == 'username':
            return UsernameLoginStrategy()
        else:
            raise ValueError('Invalid login type')
    
    @staticmethod
    def check_conflicting_login_info(login_type, data):
        if login_type == 'email' and 'username' in data:
            return jsonify({
            'success': False,
            'message': 'Invalid request: Login type is email, but username is provided'
        }), 400
    
        if login_type == 'username' and 'email' in data:
            return jsonify({
            'success': False,
            'message': 'Invalid request: Login type is username, but email is provided'
        }), 400



class LoginStrategy:
    def login(self, data):
        raise NotImplementedError()


class EmailLoginStrategy(LoginStrategy):
    def login(self, data):
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


class UsernameLoginStrategy(LoginStrategy):
    def login(self, data):
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        usertype_id = user.usertypeid

        if user is None or not user.check_password(password):
            return jsonify({
                'success': False,
                'message': 'Invalid username or password'
            }), 401

        return jsonify({
            'success': True,
            'message': 'Logged in successfully',
            'usertype_id': usertype_id,
        }), 200

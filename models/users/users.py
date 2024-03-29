from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
import bcrypt
from request_errors import validate_date_format


doctor_patient_association = db.Table('doctor_patient_association',
                                      db.Column('doctor_id', db.Integer, db.ForeignKey(
                                          'doctor.id'), primary_key=True),
                                      db.Column('patient_id', db.Integer, db.ForeignKey(
                                          'patient.id'), primary_key=True)
                                      )

class User(BaseDbModel, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)

    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)

    usertypeid = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False)

    role = db.Column(db.Enum('secretary', 'doctor'), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, phone_number, usertypeid, role):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.role = role
        self.usertypeid = usertypeid

    def check_password(self, password):
        """Checks if the given password matches the stored password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'role': self.role
        }

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
from models.appointments.appointments import Appointment


class Patient(BaseDbModel, db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __init__(self, first_name, last_name, birth_date, phone_number, email, deleted=False):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.email = email
        self.deleted = deleted

    def format(self):
        # Return a formatted dictionary representation of the object
        formatted_dict = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'email': self.email,
            'deleted': self.deleted,
            'appointments': [a.id for a in self.appointments]
        }
        return formatted_dict

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
from models.users.users import User 
from models.appointments.appointments import Appointment
from models.clinicalitems.clinicalitems import ClinicItem

class Secretary(User):
    __tablename__ = 'secretary'

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)

    appointments = db.relationship(
        'Appointment', backref='secretary', lazy=True)
    clinic_items = db.relationship(
        'ClinicItem', backref='secretary', lazy=True)

    purchases = db.relationship('Purchase', backref='secretary', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'secretary',
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, usertypeid, phone_number):
        super().__init__(username=username, password=password, email=email, first_name=first_name,
                         last_name=last_name, birth_date=birth_date, phone_number=phone_number, usertypeid=usertypeid, role='secretary')

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

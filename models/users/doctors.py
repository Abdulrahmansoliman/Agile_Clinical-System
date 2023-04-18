from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel

from models.users.users import doctor_patient_association, User
from models.appointments.appointments import Appointment
from models.patients.patients import Patient

class Doctor(User):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    specialization = db.Column(db.String(50), nullable=False)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    patients = db.relationship(
        'Patient', secondary=doctor_patient_association, backref='doctors', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, phone_number, specialization):
        super().__init__(username=username, password=password, email=email, first_name=first_name,
                         last_name=last_name, birth_date=birth_date, phone_number=phone_number, role='doctor')
        self.specialization = specialization

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'role': self.role,
            'specialization': self.specialization
        }

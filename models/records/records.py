from datetime import datetime
from collections import OrderedDict
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
from models.users.users import User
from models.patients.patients import Patient


class Record(BaseDbModel, db.Model):
    __tablename__ = 'record'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    marital_status = db.Column(db.String(50), nullable=True)
    notes = db.Column(db.String(500), nullable=True)

    # Define relationships with other tables
    lab_tests = db.relationship('LabTest', backref='record', lazy=True)
    medications = db.relationship('Medication', backref='record', lazy=True)
    medical_histories = db.relationship(
        'MedicalHistory', backref='record', lazy=True)
    allergies = db.relationship('Allergy', backref='record', lazy=True)

    # Define foreign keys
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_profile_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def __init__(self, date, marital_status=None, notes=None, doctor_id=None, patient_profile_id=None):
        # Initialize object with given values
        self.date = date
        self.marital_status = marital_status
        self.notes = notes
        self.doctor_id = doctor_id
        self.patient_profile_id = patient_profile_id

    def format(self):
        # Return a formatted dictionary representation of the object
        formatted_dict = {
            'id': self.id,
            'date': self.date,
            'marital_status': self.marital_status,
            'notes': self.notes,
            'doctor_id': self.doctor_id,
            'patient_profile_id': self.patient_profile_id,
        }
        return formatted_dict

    def arr_format(self):
        # Return a formatted dictionary representation of the object without deleted flag
        formatted_dict = {
            'lab_tests': [lt.format() for lt in self.lab_tests],
            'medications': [m.format() for m in self.medications],
            'medical_histories': [mh.format() for mh in self.medical_histories],
            'allergies': [a.format() for a in self.allergies]
        }
        return formatted_dict

from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel

class Appointment(BaseDbModel, db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey(
        'doctor.id'), nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey(
        'secretary.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(500), nullable=True)

    def __init__(self, patient_id, doctor_id, secretary_id, start_time, end_time, notes=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.secretary_id = secretary_id
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

    def format(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'secretary_id': self.secretary_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'notes': self.notes
        }

from datetime import datetime
from collections import OrderedDict
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
from flask import abort, jsonify
from models.records.reportentities import ReportEntity



class Record(BaseDbModel, db.Model):
    __tablename__ = 'record'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    marital_status = db.Column(db.String(50), nullable=True)
    notes = db.Column(db.String(500), nullable=True)

    # backref to report
    reports = db.relationship('Report', lazy='subquery', backref = 'record')

    # Define foreign keys
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_profile_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def __init__(self, date, patient_profile_id, marital_status=None, notes=None, doctor_id=None):
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
            'reports': self.get_reports()
        }
        return formatted_dict

    def get_reports_entities(self):
        # Return a list containing the report entities of the record without duplicates
        entities = [report.get_entities() for report in self.reports]
        distinct_entities = []
        for entity in entities:
            if entity not in distinct_entities:
                distinct_entities.append(entity)
        return distinct_entities


    def get_reports(self):
        # Return a formatted dictionary representation of the object without deleted flag
        values = [v.format() for v in self.reports]
        return values

    def delete(self):
        # delete all reports of the record
        for report in self.reports:
            report.delete()
        return super().delete()
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel

from models.records.records import Record    


class MedicalHistory(BaseDbModel, db.Model):
    __tablename__ = 'medical_history'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    record_id = db.Column(db.Integer, db.ForeignKey(
        'record.id'), nullable=False)

    def __init__(self, date, notes):
        # Initialize instance variables
        self.date = date
        self.notes = notes

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'date': self.date,
            'notes': self.notes
        }

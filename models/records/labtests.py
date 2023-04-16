from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel
from models.records.records import Record


class LabTest(BaseDbModel, db.Model):
    __tablename__ = 'lab_test'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey(
        'record.id'), nullable=False)

    def __init__(self, name, result, date):
        # Initialize instance variables
        self.name = name
        self.result = result
        self.date = date

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'name': self.name,
            'result': self.result,
            'date': self.date
        }

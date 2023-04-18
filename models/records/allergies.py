from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel

from models.records.records import Record


class Allergy(BaseDbModel, db.Model):
    __tablename__ = 'allergy'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    allergen = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'))

    def __init__(self, name, allergen, description=None):
        # Initialize instance variables
        self.name = name
        self.allergen = allergen
        self.description = description

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'name': self.name,
            'allergen': self.allergen,
            'description': self.description,
            'record_id': self.record_id
        }

        
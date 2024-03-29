from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from models.init import db, BaseDbModel


class ClinicItem(BaseDbModel, db.Model):
    __tablename__ = 'clinic_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey(
        'secretary.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, quantity, secretary_id, price):
        self.name = name
        self.quantity = quantity
        self.secretary_id = secretary_id
        self.price = price

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'secretary_id': self.secretary_id
        }

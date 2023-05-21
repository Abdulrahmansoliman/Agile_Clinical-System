from models.init import db, BaseDbModel
from models.clinicalitems.purchasedetails import PurchaseDetail

class Purchase(BaseDbModel, db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patient.id'), nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey(
        'secretary.id'), nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    purchase_details = db.relationship('PurchaseDetail', backref='purchase', lazy=True)

    def __init__(self, patient_id, secretary_id, total_quantity, date):
        self.patient_id = patient_id
        self.secretary_id = secretary_id
        self.total_quantity = total_quantity
        self.date = date

    def format(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'secretary_id': self.secretary_id,
            'total_quantity': self.total_quantity,
            'date': self.date
        }
    
    def format_with_items(self):
        items = [item.format() for item in PurchaseDetail.query.filter_by(purchase_id=self.id).all()]
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'secretary_id': self.secretary_id,
            'total_quantity': self.total_quantity,
            'date': self.date,
            'items': items
        }
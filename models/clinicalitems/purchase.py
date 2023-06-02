from models.init import db, BaseDbModel
from models.clinicalitems.purchasedetails import PurchaseDetail

class Purchase(BaseDbModel, db.Model):
    __tablename__ = 'purchase'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(
        'patient.id'), nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey(
        'secretary.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    purchase_details = db.relationship('PurchaseDetail', backref='purchase', lazy=True)

    def __init__(self, patient_id, secretary_id):
        self.patient_id = patient_id
        self.secretary_id = secretary_id
        self.date  = db.func.current_timestamp()

    def calculate_total_quantity(self):
        self.total_quantity = sum([item.quantity for item in PurchaseDetail.query.filter_by(purchase_id=self.id).all()])
        
    def get_items(self):
        return [item.format() for item in PurchaseDetail.query.filter_by(purchase_id=self.id).all()]
    
    def calculate_total_price(self):
        self.total_price = sum([item.price for item in PurchaseDetail.query.filter_by(purchase_id=self.id).all()])
    
    def format(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'secretary_id': self.secretary_id,
            'total_quantity': self.calculate_total_quantity(),
            'total_price': self.calculate_total_price(),
            'date': self.date
        }
    
    def format_with_items(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'secretary_id': self.secretary_id,
            'total_quantity': self.total_quantity,
            'total_price': self.total_price,
            'date': self.date,
            'items': self.get_items()
        }
    
    
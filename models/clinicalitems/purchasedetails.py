from models.init import db, BaseDbModel
from models.clinicalitems.clinicalitems import ClinicItem

class PurchaseDetail(BaseDbModel, db.Model):
    __tablename__ = 'purchase_detail'

    id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, db.ForeignKey(
        'purchase.id'), nullable=False)
    clinic_item_id = db.Column(db.Integer, db.ForeignKey(
        'clinic_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, purchase_id, clinic_item_id, quantity):
        self.purchase_id = purchase_id
        self.clinic_item_id = clinic_item_id
        self.quantity = quantity
        self.price = ClinicItem.query.get(clinic_item_id).price * quantity
    
    def format(self):
        return {
            'id': self.id,
            'purchase_id': self.purchase_id,
            'clinic_item_id': self.clinic_item_id,
            'quantity': self.quantity,
            'price': self.price
        }
    
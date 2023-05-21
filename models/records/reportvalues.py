from models.init import db, BaseDbModel

class ReportValue(BaseDbModel, db.Model):
    __tablename__ = 'report_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)
    entity_attribute_id = db.Column(db.Integer, db.ForeignKey(
        'entity_attribute.id'), nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey(
        'record.id'), nullable=False)
    
    # entity_attribute_id and record_id uniquely identify a report value
    __table_args__ = (db.UniqueConstraint('entity_attribute_id', 'record_id', name='uix_1'),)

    def __init__(self, value, entity_attribute_id, record_id):
        self.value = value
        self.entity_attribute_id = entity_attribute_id
        self.record_id = record_id

    def format(self):
        return {
            'id': self.id,
            'value': self.value,
            'entity_attribute_id': self.entity_attribute_id,
            'record_id': self.record_id
        }
    

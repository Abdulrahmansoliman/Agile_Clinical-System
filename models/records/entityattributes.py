from models.init import db, BaseDbModel

class EntityAttribute(BaseDbModel, db.Model):
    __tablename__ = 'entity_attribute'

    id = db.Column(db.Integer, primary_key=True)
    report_attribute_id = db.Column(db.Integer, db.ForeignKey(
        'report_attribute.id'), nullable=False)
    report_entity_id = db.Column(db.Integer, db.ForeignKey(
        'report_entity.id'), nullable=False)
    
    # backref to report_value
    report_values = db.relationship('ReportValue', backref='entity_attribute', lazy=True)
    
    # report_attribute_id and report_entity_id uniquely identify an entity attribute
    __table_args__ = (db.UniqueConstraint('report_attribute_id', 'report_entity_id', name='uix_1'),)
    
    def __init__(self, report_attribute_id, report_entity_id):
        self.report_attribute_id = report_attribute_id
        self.report_entity_id = report_entity_id

    def format(self):
        return {
            'id': self.id,
            'report_attribute_id': self.report_attribute_id,
            'report_entity_id': self.report_entity_id
        }
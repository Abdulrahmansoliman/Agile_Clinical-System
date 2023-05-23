from models.init import db, BaseDbModel


class ReportValue(BaseDbModel, db.Model):
    __tablename__ = 'report_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)
    report_entity_id = db.Column(db.Integer, db.ForeignKey('report_entity.id'), nullable=False)
    report_attribute_id = db.Column(db.Integer, db.ForeignKey('report_attribute.id'), nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)

    # define unique constraint on report_entity_id, report_attribute_id, record_id
    __table_args__ = (db.UniqueConstraint('report_entity_id', 'report_attribute_id', 'record_id', name='_report_entity_attribute_record_uc'),)

    def __init__(self, value, report_entity_id, report_attribute_id, record_id):
        self.value = value
        self.report_entity_id = report_entity_id
        self.report_attribute_id = report_attribute_id
        self.record_id = record_id

    def format(self):
        return {
            'id': self.id,
            'value': self.value,
            'report_entity_id': self.report_entity_id,
            'report_attribute_id': self.report_attribute_id,
            'record_id': self.record_id
        }
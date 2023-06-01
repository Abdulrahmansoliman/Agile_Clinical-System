from models.init import db, BaseDbModel
from models.records.reportattributes import ReportAttribute


class ReportValue(BaseDbModel, db.Model):
    __tablename__ = 'report_value'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)
    report_entity_id = db.Column(db.Integer, db.ForeignKey('report_entity.id'), nullable=False)
    report_attribute_id = db.Column(db.Integer, db.ForeignKey('report_attribute.id'), nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)

    # define unique constraint on report_entity_id, report_attribute_id, report_id
    __table_args__ = (db.UniqueConstraint('report_entity_id', 'report_attribute_id', 'report_id', name='_report_entity_attribute_report_uc'),)

    def __init__(self, value, report_entity_id, report_attribute_id, report_id):
        self.value = value
        self.report_entity_id = report_entity_id
        self.report_attribute_id = report_attribute_id
        self.report_id = report_id

    def format(self):
        return {
            'id': self.id,
            'value': self.value,
            'value_name': ReportAttribute.query.get(self.report_attribute_id).name,
            'report_entity_id': self.report_entity_id,
            'report_attribute_id': self.report_attribute_id,
            'report_id': self.report_id
        }
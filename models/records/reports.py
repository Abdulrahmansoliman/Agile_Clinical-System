from models.init import db, BaseDbModel
from models.records.reportentities import ReportEntity

class Report(BaseDbModel, db.Model):
    __tablename__ = 'report'

    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)
    report_entity_id = db.Column(db.Integer, db.ForeignKey('report_entity.id'), nullable=False)

    # backref to report_value
    values = db.relationship('ReportValue', lazy='subquery', backref = 'report')

    def __init__(self, record_id, report_entity_id):
        self.record_id = record_id
        self.report_entity_id = report_entity_id

    def format(self):
        return {
            'id': self.id,
            'record_id': self.record_id,
            'report_entity_id': self.report_entity_id,
            'entity_name': ReportEntity.query.get(self.report_entity_id).name,
            'values': self.get_values()
        }
    
    def get_values(self):
        return [value.format() for value in self.values]
    

    def get_entities(self):
        return {
            'entity_id': self.report_entity_id,
            'entity_name': ReportEntity.query.get(self.report_entity_id).name,
        }

    def delete(self):
        # delete all values
        for value in self.values:
            value.delete()
        return super().delete()
        
from models.init import db, BaseDbModel
from models.records.reportattributes import ReportAttribute
from models.records.entityattributes import EntityAttribute

class ReportEntity(BaseDbModel, db.Model):
    __tablename__ = 'report_entity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
   
    # backref to entity_attribute
    entity_attributes = db.relationship('EntityAttribute', backref='report_entity', lazy=True)

    def __init__(self, name):
        self.name = name
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def get_attributes(self):
        EA = EntityAttribute.query.filter_by(report_entity_id=self.id).all()
        return [ReportAttribute.query.get(ea.report_attribute_id) for ea in EA]
    
    def format_with_attributes(self):
        return {
            'id': self.id,
            'name': self.name,
            'attributes': self.get_attributes()
        }
from models.init import db, BaseDbModel
from models.records.reportattributes import ReportAttribute

entity_attribute_association = db.Table('entity_attribute',
    db.Column('report_entity_id', db.Integer, db.ForeignKey('report_entity.id'), primary_key=True),
    db.Column('report_attribute_id', db.Integer, db.ForeignKey('report_attribute.id'), primary_key=True)
)
                            

class ReportEntity(BaseDbModel, db.Model):
    __tablename__ = 'report_entity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
   
    # backref to entity_attribute
    attributes = db.relationship('ReportAttribute', secondary=entity_attribute_association, lazy='subquery', backref = 'report_entities')

    def __init__(self, name):
        self.name = name
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def get_attributes(self):
        return [attribute.format() for attribute in self.attributes]
    
    def format_with_attributes(self):
        return {
            'id': self.id,
            'name': self.name,
            'attributes': self.get_attributes()
        }
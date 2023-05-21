from models.init import db, BaseDbModel

class ReportAttribute(BaseDbModel, db.Model):
    __tablename__ = 'report_attribute'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)

    # backref to entity_attribute
    entity_attributes = db.relationship('EntityAttribute', backref='report_attribute', lazy=True)

    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type
        }
    

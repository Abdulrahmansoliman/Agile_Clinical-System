from models.init import db, BaseDbModel
from models.links.links import Link

usertype_link = db.Table('usertype_link',
    db.Column('usertype_id', db.Integer, db.ForeignKey('user_type.id'), primary_key=True),
    db.Column('link_id', db.Integer, db.ForeignKey('link.id'), primary_key=True)
)
                          

class UserType(BaseDbModel, db.Model):
    __tablename__ = 'user_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='user_type', lazy=True)
    linking = db.relationship('Link', secondary=usertype_link, lazy='subquery', backref = 'user_types')

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
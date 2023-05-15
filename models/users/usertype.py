from models.init import db, BaseDbModel

class UserType(BaseDbModel, db.Model):
    __tablename__ = 'user_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='user_type', lazy=True)

    def __init__(self, name):
        self.name = name

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
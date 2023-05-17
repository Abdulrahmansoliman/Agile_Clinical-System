from models.init import db, BaseDbModel

class Link(BaseDbModel, db.Model):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
        }
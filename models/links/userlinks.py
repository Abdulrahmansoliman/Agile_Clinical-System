from models.init import db, BaseDbModel

class UserLink(BaseDbModel, db.Model):
    __tablename__ = 'userlinks'

    linkid = db.Column(db.Integer, db.ForeignKey('link.id'), primary_key=True)
    usertypeid = db.Column(db.Integer, db.ForeignKey('user_type.id'), primary_key=True)

    link = db.relationship('Link', backref='userlinks', lazy=True)

    def __init__(self, linkid, usertypeid):
        self.linkid = linkid
        self.usertypeid = usertypeid
    
    def format(self):
        return {
            'linkid': self.linkid,
            'usertypeid': self.usertypeid
        }
    
    def format_with_link(self):
        return {
            'link': self.link.format()
        }
    
    def format_with_usertype(self):
        return {
            'usertype': self.usertype.format()
        }
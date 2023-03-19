from sentry_sdk import capture_exception
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseDbModel:
    # TODO: log errors
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            capture_exception(e)
            db.session.rollback()
            raise e

    def update(self):
        try:
            db.session.commit()
        except Exception as e:
            capture_exception(e)
            db.session.rollback()
            raise e

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            capture_exception(e)
            db.session.rollback()
            raise e
        


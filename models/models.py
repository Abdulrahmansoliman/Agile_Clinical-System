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
        

doctor_patient_association = db.Table('doctor_patient_association',
                                      db.Column('doctor_id', db.Integer, db.ForeignKey(
                                          'doctor.id'), primary_key=True),
                                      db.Column('patient_id', db.Integer, db.ForeignKey(
                                          'patient.id'), primary_key=True)
                                      )


class User(BaseDbModel, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)

    role = db.Column(db.Enum('secretary', 'doctor'), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, phone_number, role):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.role = role

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'role': self.role
        }


class Doctor(User):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    specialization = db.Column(db.String(50), nullable=False)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    patients = db.relationship(
        'Patient', secondary=doctor_patient_association, backref='doctors', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, phone_number, specialization):
        super().__init__(username=username, password=password, email=email, first_name=first_name,
                         last_name=last_name, birth_date=birth_date, phone_number=phone_number, role='doctor')
        self.specialization = specialization

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'role': self.role,
            'specialization': self.specialization
        }


class Secretary(User):
    __tablename__ = 'secretary'

    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    appointments = db.relationship(
        'Appointment', backref='secretary', lazy=True)
    clinic_items = db.relationship(
        'ClinicItem', backref='secretary', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'secretary',
    }

    def __init__(self, username, password, email, first_name, last_name, birth_date, phone_number):
        super().__init__(username=username, password=password, email=email, first_name=first_name,
                         last_name=last_name, birth_date=birth_date, phone_number=phone_number, role='secretary')

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'role': self.role
        }

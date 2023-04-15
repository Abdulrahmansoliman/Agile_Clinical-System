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
    username = db.Column(db.String(50), nullable=False)

    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

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

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
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

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)

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

class Appointment(BaseDbModel, db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey('secretary.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(500), nullable=True)

    def __init__(self, patient_id, doctor_id, secretary_id, start_time, end_time, notes=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.secretary_id = secretary_id
        self.start_time = start_time
        self.end_time = end_time
        self.notes = notes

    def format(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'secretary_id': self.secretary_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'notes': self.notes
        }

class Patient(BaseDbModel, db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __init__(self, first_name, last_name, birth_date, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.email = email

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'phone_number': self.phone_number,
            'email': self.email,
            'appointments': [a.id for a in self.appointments]
        }

class ClinicItem(BaseDbModel, db.Model):
    __tablename__ = 'clinic_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    secretary_id = db.Column(db.Integer, db.ForeignKey('secretary.id'), nullable=False)

    def __init__(self, name, quantity, secretary_id):
        self.name = name
        self.quantity = quantity
        self.secretary_id = secretary_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'secretary_id': self.secretary_id
        }
    
    
class Record(BaseDbModel, db.Model):
    __tablename__ = 'record'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    marital_status = db.Column(db.String(50), nullable=True)
    notes = db.Column(db.String(500), nullable=True)

    # Define relationships with other tables
    lab_tests = db.relationship('LabTest', backref='record', lazy=True)
    medications = db.relationship('Medication', backref='record', lazy=True)
    medical_histories = db.relationship('MedicalHistory', backref='record', lazy=True)
    allergies = db.relationship('Allergy', backref='record', lazy=True)

    # Define foreign keys
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_profile_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def __init__(self, date, marital_status=None, notes=None):
        # Initialize object with given values
        self.date = date
        self.marital_status = marital_status
        self.notes = notes

    def format(self):
        # Return a formatted dictionary representation of the object
        return {
            'id': self.id,
            'date': self.date,
            'marital_status': self.marital_status,
            'notes': self.notes,
            'lab_tests': [lt.format() for lt in self.lab_tests],
            'medications': [m.format() for m in self.medications],
            'medical_histories': [mh.format() for mh in self.medical_histories],
            'allergies': [a.format() for a in self.allergies],
            'doctor_id': self.doctor_id,
            'patient_profile_id': self.patient_profile_id
        }



class LabTest(BaseDbModel, db.Model):
    __tablename__ = 'lab_test'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(50), nullable=True)
    date = db.Column(db.Date, nullable=False)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)

    def __init__(self, name, result, date):
        # Initialize instance variables
        self.name = name
        self.result = result
        self.date = date

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'name': self.name,
            'result': self.result,
            'date': self.date
        }

         

class MedicalHistory(BaseDbModel, db.Model):
    __tablename__ = 'medical_history'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)

    def __init__(self, date, notes):
        # Initialize instance variables
        self.date = date
        self.notes = notes

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'date': self.date,
            'notes': self.notes
        }

    
class Medication(BaseDbModel, db.Model):
    __tablename__ = 'medication'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'), nullable=False)

    def __init__(self, date, notes=None):
        # Initialize instance variables
        self.date = date
        self.notes = notes

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'date': self.date,
            'notes': self.notes
        }


class Allergy(BaseDbModel, db.Model):
    __tablename__ = 'allergy'

    # Define table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    allergen = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    record_id = db.Column(db.Integer, db.ForeignKey('record.id'))

    def __init__(self, name, allergen, description=None):
        # Initialize instance variables
        self.name = name
        self.allergen = allergen
        self.description = description

    def format(self):
        # Format instance variables as dictionary
        return {
            'id': self.id,
            'name': self.name,
            'allergen': self.allergen,
            'description': self.description,
            'record_id': self.record_id
        }

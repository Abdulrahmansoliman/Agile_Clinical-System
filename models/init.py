from sentry_sdk import capture_exception

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


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

from models.appointments.appointments import Appointment
from models.clinicalitems.clinicalitems import ClinicItem
from models.patients.patients import Patient
from models.users.secretaries import Secretary
from models.users.doctors import Doctor
from models.users.users import User
from models.users.users import doctor_patient_association
from models.records.records import Record
from models.records.medicalhistories import MedicalHistory
from models.records.medications import Medication
from models.records.allergies import Allergy
from models.records.labtests import LabTest
from models.users.usertypes import UserType
from models.links.links import Link
from models.links.userlinks import UserLink
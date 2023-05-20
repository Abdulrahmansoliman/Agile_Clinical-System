from flask import abort, jsonify

from models.patients.patients import Patient

def validate_patient_id(patient_id):
    patient = Patient.query.get(patient_id)
    if patient is None or patient.is_deleted == True:
        error_message = "No patient with id {} found".format(patient_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))
from flask import abort, jsonify
from models.clinicalitems.clinicalitems import ClinicItem


def validate_clinicitem_id(clinicitem_id):
    clinicitem = ClinicItem.query.get(clinicitem_id)
    if clinicitem is None or clinicitem.is_deleted == True:
        error_message = "No item with id {} found".format(clinicitem_id)
        print(error_message)
        abort(jsonify({
            "status": 404,
            "message": error_message
        }))

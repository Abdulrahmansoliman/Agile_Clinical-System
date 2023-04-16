from flask import (Blueprint,jsonify)
import sys
from models.clinicalitems.clinicalitems import ClinicItem

from routes.clinicitems.utils import validate_clinicitem_id
from request_errors import requires_body

clinicitems_blueprint = Blueprint('clinicitems', __name__)

@clinicitems_blueprint.route('/', methods=['GET'])
def get_clinicitems():
    clinicitems = ClinicItem.query.all()
    return jsonify({
        'success': True,
        'data': [c.format() for c in clinicitems]
    }), 200

@clinicitems_blueprint.route('/<int:clinicitem_id>', methods=['GET'])
def get_clinicitem(clinicitem_id):
        
        validate_clinicitem_id(clinicitem_id)
        clinicitem = ClinicItem.query.get(clinicitem_id)
        
        return jsonify({
            "success": True,
            "clinicitem": clinicitem.format()
        }), 200
        
@clinicitems_blueprint.route('/', methods=['POST'])
@requires_body("[name] [quantity] [secretary_id]")
def add_clinicitems(data):
    
    clinicitem = ClinicItem(**data)
    clinicitem.insert()
    
    return jsonify({
        "success": True,
        "clinicitem": clinicitem.format()
    }), 201    
    
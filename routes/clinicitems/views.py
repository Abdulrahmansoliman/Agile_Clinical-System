from flask import (Blueprint, jsonify)
import sys
from models.clinicalitems.clinicalitems import ClinicItem

from routes.clinicitems.utils import validate_clinicitem_id
from request_errors import requires_body
from routes.RouteFactory import RouteFactory

clinicitems_blueprint = Blueprint('clinicitems', __name__)

clinicitems_factory = RouteFactory(clinicitems_blueprint)

clinicitems_factory.generate_get_all_route(ClinicItem)
clinicitems_factory.get_one_route(ClinicItem)
clinicitems_factory.create_one_route(ClinicItem)


@clinicitems_blueprint.route('/', methods=['POST'])
@requires_body("[name] [quantity] [secretary_id]")
def add_clinicitems(data):
    clinicitem = ClinicItem(**data)
    clinicitem.insert()

    return jsonify({
        "success": True,
        "clinicitem": clinicitem.format()
    }), 201


@clinicitems_blueprint.route('/<int:clinicitem_id>', methods=['PATCH'])
@requires_body("[name] [quantity] [secretary_id]")
def edit_clinicalitems(data, clinicitem_id):
    print(data)
    validate_clinicitem_id(clinicitem_id)

    clinicitem = ClinicItem.query.get(clinicitem_id)

    clinicitem.name = data['name']
    clinicitem.quantity = data['quantity']
    clinicitem.secretary_id = data['secretary_id']

    clinicitem.update()

    return jsonify({
        "suceess": True,
        "clinicitem": clinicitem.format(),
    }), 200


@clinicitems_blueprint.route('/<int:clinicitem_id>', methods=['DELETE'])
def delete_clinicitem(clinicitem_id):

    validate_clinicitem_id(clinicitem_id)

    clinicitem = ClinicItem.query.get(clinicitem_id)

    clinicitem.delete()

    return jsonify({
        "success": True,
        "item_deleted": clinicitem.format()
    }), 200

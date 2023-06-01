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
clinicitems_factory.delete_one_route(ClinicItem)


@clinicitems_blueprint.route('/', methods=['POST'])
@requires_body("[name] [quantity] [secretary_id]")
def add_clinicitems(data):
    add = clinicitems_factory.create_one_route(ClinicItem)
    return add (data)

@clinicitems_blueprint.route('/<int:clinicitem_id>', methods=['PATCH'])
@requires_body("[name] [quantity] [secretary_id]")
def edit_clinicalitems(data, clinicitem_id):
    update = clinicitems_factory.update_one_route(ClinicItem, clinicitem_id)
    return update(data)

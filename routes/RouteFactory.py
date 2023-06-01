from flask import jsonify, Blueprint, abort
from models.init import *
from request_errors import requires_body


class RouteFactory:


    def __init__(self, blueprint):
        self.blueprint = blueprint
            
        
        self.blueprint = blueprint
    def validate_item(self, model, item_id):
        item = model.query.get(item_id)
        if item is None or item.is_deleted:
            error_message = f"No item with id {item_id} found"
            print(error_message)
            abort(jsonify({
                "status": 404,
                "message": error_message
            }))
 
    def generate_get_all_route(self, model):
        def get_all():
            items = model.query.filter_by(is_deleted=False).all()
            return jsonify({
                'success': True,
                'data': [i.format() for i in items]
            }), 200

        self.blueprint.route('/', methods=['GET'])(get_all)

    def get_one_route(self, model):
        def get_one(id):
            self.validate_item(model, id)
            item = model.query.get(id)
            return jsonify({
                'success': True,
                'data': item.format()
            }), 200
        self.blueprint.route('/<int:id>', methods=['GET'])(get_one)
    
    def create_one_route(self, model):
        def create(data):
            item = model(**data)
            item.insert()
            return jsonify({
                'success': True,
                'data': item.format()
            }), 201
        return create
        
    def update_one_route(self, model, item_id):
        def update(data):
            item = model.query.get(item_id)
            if not item:
                return jsonify({
                    'success': False,
                    'message': f"{model.__name__} not found"
                }), 404
            for key, value in data.items():
                setattr(item, key, value)
            item.update()
            return jsonify({
                'success': True,
                'data': item.format()
            }), 200
        return update

    def delete_one_route(self, model):
        def delete_id(id):
            self.validate_item(model,id)
            item = model.query.get(id)
            item.delete()
            return jsonify({
                'success': True,
                'id_deleted': id
            }), 200
        self.blueprint.route('/<int:id>', methods=['DELETE'])(delete_id)

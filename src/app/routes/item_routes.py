from flask import Blueprint, jsonify, request
from app.services import item_service
from app.schemas.item import ItemSchema

bp = Blueprint('items', __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

@bp.route('/', methods=['GET'])
def get_items():
    items = item_service.get_all_items()
    return items_schema.jsonify(items)

@bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = item_service.get_item_by_id(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return item_schema.jsonify(item)

@bp.route('/', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = item_service.add_item(data)
    return item_schema.jsonify(new_item), 201

@bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    updated_item = item_service.update_item(item_id, data)
    if not updated_item:
        return jsonify({"error": "Item not found"}), 404
    return item_schema.jsonify(updated_item)

@bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    deleted_item = item_service.delete_item(item_id)
    if not deleted_item:
        return jsonify({"error": "Item not found"}), 404
    return item_schema.jsonify(deleted_item)
from flask import Blueprint, jsonify, request
from app.services import location_service
from app.schemas.location import LocationSchema
from app.schemas.bin import BinSchema
from app.schemas.item import ItemSchema

bp = Blueprint('locations', __name__)
location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
bins_schema = BinSchema(many=True)
items_schema = ItemSchema(many=True)

@bp.route('/', methods=['GET'])
def get_locations():
    locations = location_service.get_all_locations()
    return locations_schema.jsonify(locations)

@bp.route('/<int:location_id>', methods=['GET'])
def get_location(location_id):
    location = location_service.get_location_by_id(location_id)
    if not location:
        return jsonify({"error": "Location not found"}), 404
    return location_schema.jsonify(location)

@bp.route('/', methods=['POST'])
def add_location():
    data = request.get_json()
    new_location = location_service.add_location(data)
    return location_schema.jsonify(new_location), 201

@bp.route('/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    data = request.get_json()
    updated_location = location_service.update_location(location_id, data)
    if not updated_location:
        return jsonify({"error": "Location not found"}), 404
    return location_schema.jsonify(updated_location)

@bp.route('/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    deleted_location = location_service.delete_location(location_id)
    if not deleted_location:
        return jsonify({"error": "Location not found"}), 404
    return location_schema.jsonify(deleted_location)

## Relationships

@bp.route('/<int:location_id>/bins', methods=['GET'])
def get_bins_by_location(location_id):
    bins = location_service.get_bins_by_location(location_id)
    if bins is None:
        return jsonify({"error": "Location not found"}), 404
    return bins_schema.jsonify(bins)

@bp.route('/<int:location_id>/items', methods=['GET'])
def get_items_by_location(location_id):
    items = location_service.get_bins_by_location(location_id)
    if items is None:
        return jsonify({"error": "Location not found"}), 404
    return items_schema.jsonify(items)
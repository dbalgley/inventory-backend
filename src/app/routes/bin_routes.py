from flask import Blueprint, jsonify, request
from app.services import bin_service
from app.schemas.bin import BinSchema
from app.schemas.item import ItemSchema

bp = Blueprint('bins', __name__)
bin_schema = BinSchema()
bins_schema = BinSchema(many=True)
items_schema = ItemSchema(many=True)

@bp.route('/', methods=['GET'])
def get_bins():
    bins = bin_service.get_all_bins()
    return bins_schema.jsonify(bins)

## Relationships

@bp.route('/<int:bin_id>/items', methods=['GET'])
def get_bins_by_location(bin_id):
    items = bin_service.get_items_by_bin(bin_id)
    if items is None:
        return jsonify({"error": "Bin not found"}), 404
    return items_schema.jsonify(items)
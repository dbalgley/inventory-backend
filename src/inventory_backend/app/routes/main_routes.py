import logging

from flask import render_template, current_app, jsonify
from flask_cors import cross_origin

from inventory_backend.app.routes import bp
from inventory_backend.app.models.item import Item

logger = logging.getLogger('main_routes')

@bp.route('/')
@cross_origin(origins='*')
def index():
    return render_template('index.html')

# @bp.route('/items', methods=['POST'])
# def create_item():
#     data = request.json

#     # Save image to S3 and get the new URL
#     s3 = boto3.client('s3')
#     image = request.files['image']
#     image_url = f"https://{bucket_name}.s3.amazonaws.com/{image.filename}"
#     s3.upload_fileobj(image, bucket_name, image.filename)

#     # Save item to db
#     item = 

@bp.route('/items')
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])
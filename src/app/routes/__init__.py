from flask import Blueprint

bp = Blueprint('main', __name__)

from .main_routes import bp as main_routes_bp
from .item_routes import bp as item_routes_bp

# Register blueprints with main blueprint
bp.register_blueprint(main_routes_bp)
bp.register_blueprint(item_routes_bp, url_prefix='/items')

#from . import routes
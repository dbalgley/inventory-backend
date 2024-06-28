from flask import Blueprint

bp = Blueprint('main', __name__)

from .main_routes import bp as main_routes_bp
from .item_routes import bp as item_routes_bp
from .location_routes import bp as location_routes_bp
from .bin_routes import bp as bin_routes_bp

# Register blueprints with main blueprint
bp.register_blueprint(main_routes_bp)
bp.register_blueprint(item_routes_bp, url_prefix='/items')
bp.register_blueprint(location_routes_bp, url_prefix='/locations')
bp.register_blueprint(bin_routes_bp, url_prefix='/bins')

#from . import routes
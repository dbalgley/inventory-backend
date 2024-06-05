from flask import Blueprint

bp = Blueprint('main', __name__)

from .main_routes import bp as main_routes_bp

#from . import routes
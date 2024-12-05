
import logging

from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

from app.config import Config
from app.models import db

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)

def create_app(config_class:type[Config]=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app
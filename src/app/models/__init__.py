from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .item import Item
from .location import Location
from .bin import Bin
from os import environ

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'a-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://inventory_user:scavenger@localhost:5432/inventory_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
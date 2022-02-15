import os


class Config(object):
    DEBUG = os.environ.get("APP_DEBUG")
    ENV = os.environ.get("FLASK_ENV")
    TESTING = os.environ.get("APP_TESTING")
    CSRF_ENABLED = os.environ.get("CSRF_ENABLED")
    SECRET_KEY = os.environ.get("APP_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

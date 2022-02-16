from flask import Flask
from .database import init_db
from .api import init_apis


def init_extensions(app: Flask):
    init_db(app)
    init_apis(app)

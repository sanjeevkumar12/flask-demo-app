from flask import Blueprint, Flask
from flask_restx import Api, Namespace

from app.conf import API_BLUEPRINTS
from app.extensions import api, api_bp


def init_apis(app: Flask):
    app.register_blueprint(api_bp)
    for api_blueprint in API_BLUEPRINTS:
        if isinstance(api_blueprint, Blueprint):
            api_bp.register_blueprint(api_blueprint)
        elif isinstance(api_blueprint, Namespace):
            api.add_namespace(api_blueprint)

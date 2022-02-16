from flask import Blueprint, Flask
from flask_apispec import FlaskApiSpec
from app import conf
import importlib

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api_docs = FlaskApiSpec()


def init_apis(app: Flask):
    for api_blueprint in conf.API_BLUEPRINTS:
        module_name, class_name = api_blueprint.rsplit(".", 1)
        module = importlib.import_module(module_name)
        assert hasattr(module, class_name), "class {} is not in {}".format(
            class_name, module_name
        )
        cls = getattr(module, class_name)
        if not isinstance(cls, Blueprint):
            raise TypeError(f"{class_name} not valid blueprint class")
        api_bp.register_blueprint(cls)
    app.register_blueprint(api_bp)
    api_docs.init_app(app)

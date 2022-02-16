from flask import Flask

from .extensions import init_extensions
from .views import home, page_not_found


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    init_extensions(app)
    app.add_url_rule("/", "home", home)
    app.register_error_handler(404, page_not_found)

    return app

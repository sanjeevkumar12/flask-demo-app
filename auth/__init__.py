from flask import Blueprint
from app.extensions.api import api_docs
from .api.views.register import RegisterUserApi

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.add_url_rule("/register", view_func=RegisterUserApi.as_view("register"))
api_docs.register(RegisterUserApi, endpoint="api.auth.register")

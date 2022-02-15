import pathlib

from auth.api.namespace import auth_ns

from .contants import BASE_DIR

API_BLUEPRINTS = [
    auth_ns,
]


MODEL_LOOKUP_EXCLUDE_DIRECTORY = ["migrations"]


__all__ = ["auth_ns", "API_BLUEPRINTS", "MODEL_LOOKUP_EXCLUDE_DIRECTORY", "BASE_DIR"]

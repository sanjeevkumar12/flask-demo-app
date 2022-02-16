import pathlib

from .contants import BASE_DIR

API_BLUEPRINTS = ["auth.auth_bp"]


MODEL_LOOKUP_EXCLUDE_DIRECTORY = ["migrations"]


__all__ = ["API_BLUEPRINTS", "MODEL_LOOKUP_EXCLUDE_DIRECTORY", "BASE_DIR"]

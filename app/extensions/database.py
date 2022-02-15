from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.scoping import scoped_session

from app.core.loaders.models import get_models, load_models

db = SQLAlchemy()
db_migration = Migrate()


def init_db(app: Flask):
    load_models()
    db.init_app(app)
    db_migration.init_app(app=app, db=db)


def register_models():
    load_models()


def get_session() -> scoped_session:
    return db.session

from flask import redirect, url_for

from app.core.http.exceptions import NotFound


def home():
    return redirect(url_for("flask-apispec.swagger-ui"))


def page_not_found(e: NotFound):
    return {"message": e.description, "code": 404}, 404

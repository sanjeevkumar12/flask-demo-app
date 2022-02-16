from http import HTTPStatus
from ..schemas.register import RegisterRequestSchema
from flask_apispec import MethodResource, marshal_with, use_kwargs, doc
from ...services import auth_repository
from app.core.http.response.schemas.base import APIErrorSchema

class RegisterUserApi(MethodResource):
    @doc(description="User Register API.", tags=["Awesome"])
    @use_kwargs(RegisterRequestSchema, location=("json"))
    #@marshal_with(APIErrorSchema, HTTPStatus.UNPROCESSABLE_ENTITY)
    @marshal_with(RegisterRequestSchema, HTTPStatus.CREATED)  # marshalling
    def post(self, **kwargs):
        kwargs.pop("confirm_password")
        user = auth_repository.get_user_by_email(kwargs.get('email'))
        if user:
            return {
                'messages': {'email' : f"{kwargs.get('email')} is not available"},
                'error': True
            }
        user = auth_repository.create(**kwargs)
        return user, HTTPStatus.CREATED

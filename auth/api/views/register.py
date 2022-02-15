import http
from http import HTTPStatus

from flask_restx import Namespace, Resource, abort

from auth.request.parsers import register_request_parser

from ...services import auth_repository
from ..namespace import auth_ns


@auth_ns.route("/register", endpoint="api_auth_register")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/register."""

    @auth_ns.expect(register_request_parser)
    @auth_ns.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @auth_ns.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @auth_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        """Register a new user and return an access token."""
        request_data = register_request_parser.parse_args()
        email = request_data.get("email")
        password = request_data.get("password")
        if auth_repository.get_user_by_email(email):
            abort(http.HTTPStatus.CONFLICT, "Email address is already registered.")
        user = auth_repository.create(email=email, password=password)
        return {"email": email, "password": password}, HTTPStatus.CREATED

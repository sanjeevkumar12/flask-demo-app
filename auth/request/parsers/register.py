from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

register_request_parser = RequestParser(bundle_errors=True)
register_request_parser.add_argument(
    name="email", type=email(), location="json", required=True, nullable=False
)
register_request_parser.add_argument(
    name="password", type=str, location="json", required=True, nullable=False
)

register_request_parser.add_argument(
    name="confirm_password",
    type=str,
    location="json",
    required=True,
    nullable=False,
    help="Password and Confirm password should have same value.",
)

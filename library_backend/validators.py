import re
from functools import wraps

from library_backend.exceptions import RequiredFieldException, InvalidFieldException


def validate_request_for_user(func):
    def func_wrapper(*args, **kwargs):
        _validate_user_payload(args[1])
        return func(*args, **kwargs)

    return func_wrapper


def handle_required_field(f):
    """
    Handle KeyError exceptions
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyError as e:
            raise RequiredFieldException(e.args[0])

    return decorated


@handle_required_field
def _validate_user_payload(body):
    regexp_email = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    if body["first_name"] is None:
        raise RequiredFieldException("first_name")
    if body["last_name"] is None:
        raise RequiredFieldException("last_name")
    if body["email"] is None:
        raise RequiredFieldException("email")
    if not re.compile(regexp_email).match(body["email"]):
        raise InvalidFieldException("email")

import re
from functools import wraps
from inspect import signature

from library_backend.exceptions import RequiredFieldException, InvalidFieldException


def validate_request_for_user(func):
    params = list(signature(func).parameters)
    second_argname = params[1]

    def func_wrapper(*args, **kwargs):
        payload = (kwargs[second_argname]
                   if second_argname in kwargs else args[1])
        _validate_user_payload(payload)
        return func(*args, **kwargs)

    return func_wrapper


def validate_request_for_book(func):
    params = list(signature(func).parameters)
    second_argname = params[1]

    def func_wrapper(*args, **kwargs):
        payload = (kwargs[second_argname]
                   if second_argname in kwargs else args[1])
        _validate_book_payload(payload)
        return func(*args, **kwargs)

    return func_wrapper


def validate_request_for_reservation(func):
    params = list(signature(func).parameters)
    second_argname = params[1]

    def func_wrapper(*args, **kwargs):
        payload = (kwargs[second_argname]
                   if second_argname in kwargs else args[1])
        _validate_reservation_payload(payload)
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
    if not body["first_name"] or body["first_name"] is None:
        raise RequiredFieldException("first_name")
    if not body["last_name"] or body["last_name"] is None:
        raise RequiredFieldException("last_name")
    if not body["email"] or body["email"] is None:
        raise RequiredFieldException("email")
    if not re.compile(regexp_email).match(body["email"]):
        raise InvalidFieldException("email")


@handle_required_field
def _validate_book_payload(body):
    if not body["name"] or body["name"] is None:
        raise RequiredFieldException("name")
    if not body["author"] or body["author"] is None:
        raise RequiredFieldException("author")


@handle_required_field
def _validate_reservation_payload(body):
    if not body["user_id"] or body["user_id"] is None:
        raise RequiredFieldException("user_id")
    if not body["book_id"] or body["book_id"] is None:
        raise RequiredFieldException("book_id")
    if not body["reservation_date"] or body["reservation_date"] is None:
        raise RequiredFieldException("reservation_date")

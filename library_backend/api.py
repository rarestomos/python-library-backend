import json
from functools import wraps

from library_backend.exceptions import *
from library_backend.service import UserService, BookService, ReservationService
from library_backend.validators import validate_request_for_user


def response(message, status_code):
    return {
        'status_code': str(status_code),
        'body': json.dumps(message)
    }


def handle_request():
    """
    Handle common exceptions.
    :return: Decorated function.
    """

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return response(f(*args, **kwargs), 200)
            except (InvalidUser,
                    InvalidBook,
                    ValueError,
                    UserAlreadyExists,
                    ResourceNotFound,
                    BookAlreadyExists,
                    ReservationAlreadyExists,
                    ReservationIsInvalid) as e:
                return response(str(e), 400)
            except KeyError as e:
                return response(f'{str(e)} is required', 400)

        return wrapper

    return decorator


class UserApi:

    @handle_request()
    @validate_request_for_user
    def create_user(self, user):
        user_service = UserService()
        user = user_service.create_user(user_dict=user)
        return user

    @handle_request()
    def list_users(self):
        user_service = UserService()
        user_list = user_service.list_users()
        return user_list

    @handle_request()
    def delete_user(self, user_id):
        user_service = UserService()
        user_service.delete_user(user_id)
        return f"Successfully deleted user {user_id}"

    @handle_request()
    def update_user(self, user_id, new_user):
        user_service = UserService()
        new_user = user_service.update_user(user_id, new_user)
        return new_user

    @handle_request()
    def get_user(self, user_id):
        user_service = UserService()
        user = user_service.get_user(user_id)
        return user


class BookApi:

    @handle_request()
    def get_books(self):
        book_service = BookService()
        return book_service.list_books()

    @handle_request()
    def create_book(self, book):
        book_service = BookService()
        return book_service.create_book(book)

    @handle_request()
    def get_book(self, book_id):
        book_service = BookService()
        return book_service.get_book(book_id)

    @handle_request()
    def update_book(self, book_id, new_book):
        book_service = BookService()
        return book_service.edit_book(book_id, new_book)

    @handle_request()
    def delete_book(self, book_id):
        book_service = BookService()
        book_service.delete_book(book_id)
        return f"Book with id {book_id} has been deleted"

    @handle_request()
    def get_books_by_name(self, book_name):
        book_service = BookService()
        return book_service.get_book_by_partial_name(book_name)

    @handle_request()
    def get_books_by_author(self, author_name):
        book_service = BookService()
        return book_service.get_book_by_partial_author_name(author_name)


class ReservationApi:

    @handle_request()
    def get_reservations(self):
        reservation_service = ReservationService()
        return reservation_service.list_reservations()

    @handle_request()
    def add_reservation(self, reservation):
        reservation_service = ReservationService()
        return reservation_service.add_reservation(reservation)

    @handle_request()
    def get_reservation_by_user_id(self, user_id):
        reservation_service = ReservationService()
        return reservation_service.get_reservation_by_user_id(user_id)

    @handle_request()
    def get_reservation_by_book_id(self, book_id):
        reservation_service = ReservationService()
        return reservation_service.get_reservation_by_book_id(book_id)

    @handle_request()
    def get_reservation_by_user_id_and_book_id(self, user_id, book_id):
        reservation_service = ReservationService()
        return reservation_service.get_reservation_by_user_id_and_book_id(user_id=user_id, book_id=book_id)

    @handle_request()
    def update_reservation(self, user_id, book_id, reservation_payload):
        reservation_service = ReservationService()
        return reservation_service.update_reservation(user_id=user_id, book_id=book_id, reservation_payload=reservation_payload)

    @handle_request()
    def delete_reservation(self, user_id, book_id):
        reservation_service = ReservationService()
        reservation_service.delete_reservation_by_user_and_book(user_id=user_id, book_id=book_id)
        return f"Deleted reservation for users {user_id} and book {book_id}"

    @handle_request()
    def delete_all_reservations_for_users(self, user_id):
        reservation_service = ReservationService()
        number = reservation_service.delete_reservations_for_user(user_id)
        return f"Deleted {number} of reservations for users {user_id}"

    @handle_request()
    def delete_all_reservation_for_book(self, book_id):
        reservation_service = ReservationService()
        reservation_service.delete_reservation_for_book(book_id=book_id)
        return f"Deleted reservation for book {book_id}"

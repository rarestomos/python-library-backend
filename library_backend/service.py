from library_backend.database import SQLiteDatabaseConnection
from library_backend.exceptions import (UserAlreadyExists,
                                        ResourceNotFound,
                                        InvalidFieldException,
                                        BookAlreadyExists,
                                        ReservationAlreadyExists,
                                        ReservationIsInvalid, DatabaseCommunicationIssue)
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.reservations_db_model import ReservationsDBModel
from library_backend.models.database.users_db_model import *


class UserService:

    def create_user(self, user_dict):
        db = SQLiteDatabaseConnection()
        with db:
            if db.get_user_by_email(user_dict["email"]):
                raise UserAlreadyExists(user_dict)
        user_model = UsersDBModel(**user_dict)
        with db:
            db.add_user(user_model)
            user_dict = db.get_user_by_email(user_model.email).serialize()
        return user_dict

    def list_users(self):
        db = SQLiteDatabaseConnection()
        with db:
            user_list = UsersDBModel.serialize_list(db.get_all_users())
        return user_list

    def get_user(self, user_id):
        db = SQLiteDatabaseConnection()
        with db:
            user = db.get_user_by_id(user_id)
            if not user:
                raise ResourceNotFound(resource_type="User", field="id", value=user_id)
            user = user.serialize()

        return user

    def delete_user(self, user_id):
        db = SQLiteDatabaseConnection()
        with db:
            rows = db.delete_user_by_id(user_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="User", field="id", value=user_id)
        return f"Successfully deleted user {user_id}"

    def update_user(self, user_id, new_user):
        old_user = self.get_user(user_id)
        new_user["id"] = old_user["id"]
        if not old_user["email"] == new_user["email"]:
            raise InvalidFieldException("email")
        db = SQLiteDatabaseConnection()
        user_model = UsersDBModel(**new_user)
        with db:
            rows = db.update_user(user_id, user_model)
        user = self.get_user(user_id)
        if rows == 0:
            raise DatabaseCommunicationIssue("update user")
        return user


class BookService:

    def create_book(self, book):
        db = SQLiteDatabaseConnection()
        with db:
            existing_book = db.get_book_by_author_and_name(author=book["author"], name=book["name"])
            if existing_book:
                raise BookAlreadyExists(book)
        book_model = BooksDBModel(**book)
        with db:
            db.add_book(book_model)
            book = db.get_book_by_author_and_name(name=book_model.name, author=book_model.author).serialize()
        return book

    def list_books(self):
        db = SQLiteDatabaseConnection()
        with db:
            books_list = BooksDBModel.serialize_list(db.get_all_books())
        return books_list

    def get_book(self, book_id):
        db = SQLiteDatabaseConnection()
        with db:
            book = db.get_book_by_id(book_id)
            if not book:
                raise ResourceNotFound(resource_type="Book", field="id", value=book_id)
            book = book.serialize()
        return book

    def edit_book(self, book_id, new_book):
        db = SQLiteDatabaseConnection()
        existing_book = self.get_book(book_id)
        if not existing_book:
            raise ResourceNotFound(resource_type="Book", field="id", value=book_id)
        new_book["id"] = book_id
        new_book_model = BooksDBModel(**new_book)
        with db:
            existing_book = db.get_book_by_author_and_name(name=new_book_model.name, author=new_book_model.author)
            if existing_book and not existing_book.id == book_id:
                raise BookAlreadyExists(new_book)
            rows = db.update_book(book_id, new_book_model)
            if rows == 0:
                raise DatabaseCommunicationIssue("update book")
        return self.get_book(book_id)

    def delete_book(self, book_id):
        db = SQLiteDatabaseConnection()
        with db:
            rows = db.delete_book_by_id(book_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="Book", field="id", value=book_id)
        return f"Successfully deleted book {book_id}"

    def get_book_by_partial_name(self, book_name):
        db = SQLiteDatabaseConnection()
        with db:
            books = db.get_book_by_partial_name(book_name)
            books_list = BooksDBModel.serialize_list(books)
        return books_list

    def get_book_by_partial_author_name(self, author_name):
        db = SQLiteDatabaseConnection()
        with db:
            books = db.get_books_by_partial_author_name(author_name)
            books_list = BooksDBModel.serialize_list(books)
        return books_list


class ReservationService:

    def __init__(self):
        self.db = SQLiteDatabaseConnection()

    def list_reservations(self):
        reservations_list = []
        with self.db:
            reservations = self.db.get_full_reserved_books_info()
            for user, book, reservation in reservations:
                reservations_list.append({"user": user.serialize(),
                                          "book": book.serialize(),
                                          "reservation_date": reservation.reservation_date,
                                          "reservation_expiration_date": reservation.reservation_expiration_date})
        return reservations_list

    def add_reservation(self, reservation_payload):
        try:
            self._validate_reservation_payload(reservation_payload)
        except Exception as e:
            raise e
        reservation = ReservationsDBModel(**reservation_payload)
        existing_reservation = self._get_reservation_by_user_id_and_book_id(reservation.user_id, reservation.book_id)
        if existing_reservation:
            raise ReservationAlreadyExists(reservation_payload)
        with self.db:
            self.db.add_reservation(reservation)
            try:
                user, book, reservation = self.db.get_reserved_book_by_user_id_and_book_id(user_id=reservation.user_id,
                                                                                           book_id=reservation.book_id)
                reservation_details = {"user": user.serialize(),
                                       "book": book.serialize(),
                                       "reservation_date": reservation.reservation_date,
                                       "reservation_expiration_date": reservation.reservation_expiration_date
                                       }
                return reservation_details
            except TypeError:
                raise ResourceNotFound(resource_type="Reservation", field="(user_id, book_id)",
                                       value=(reservation_payload['user_id'], reservation_payload['book_id']))

    def get_reservation_by_user_id_and_book_id(self, user_id, book_id):
        with self.db:
            try:
                user, book, reservation = self.db.get_reserved_book_by_user_id_and_book_id(user_id=user_id,
                                                                                           book_id=book_id)
                reservation = {"user": user.serialize(),
                               "book": book.serialize(),
                               "reservation_date": reservation.reservation_date,
                               "reservation_expiration_date": reservation.reservation_expiration_date
                               }
                return reservation
            except TypeError:
                raise ResourceNotFound(resource_type="Reservation",
                                       field="(user_id, book_id)", value=(user_id, book_id))

    def _get_reservation_by_user_id_and_book_id(self, user_id, book_id):
        try:
            return self.get_reservation_by_user_id_and_book_id(user_id=user_id, book_id=book_id)
        except ResourceNotFound:
            return None

    def get_reservation_by_user_id(self, user_id):
        reservations_list = []
        with self.db:
            reservations = self.db.get_reserved_books_by_user_id(user_id)
            for user, book, reservation in reservations:
                reservations_list.append({"user": user.serialize(),
                                          "book": book.serialize(),
                                          "reservation_date": reservation.reservation_date,
                                          "reservation_expiration_date": reservation.reservation_expiration_date
                                          })
        return reservations_list

    def get_reservation_by_book_id(self, book_id):
        reservations_list = []
        with self.db:
            reservations = self.db.get_reservation_by_book_id(book_id)
            for user, book, reservation in reservations:
                reservations_list.append({"user": user.serialize(),
                                          "book": book.serialize(),
                                          "reservation_date": reservation.reservation_date,
                                          "reservation_expiration_date": reservation.reservation_expiration_date
                                          })
        return reservations_list

    def delete_reservations_for_user(self, user_id):
        with self.db:
            rows = self.db.delete_reservation_by_user(user_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="Reservation", field="user_id", value=user_id)
        return f"Deleted {rows} reservations for user {user_id}"

    def delete_reservation_by_user_and_book(self, user_id, book_id):
        with self.db:
            rows = self.db.delete_reservation_by_user_and_book_id(user_id=user_id, book_id=book_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="Reservation", field="(user_id, book_id)", value=(user_id, book_id))
        return f"Deleted reservation for user {user_id} and book {book_id}"

    def update_reservation(self, user_id, book_id, reservation_payload):
        reservation = ReservationsDBModel(**reservation_payload)
        if not reservation.user_id == user_id or not reservation.book_id == book_id:
            raise ReservationIsInvalid({"user_id": user_id, "book_id": book_id})
        with self.db:
            rows = self.db.update_reservation(reservation)
        if rows == 0:
            raise DatabaseCommunicationIssue("update reservation")
        return self._get_reservation_by_user_id_and_book_id(user_id=reservation.user_id, book_id=reservation.book_id)

    def delete_reservation_for_book(self, book_id):
        with self.db:
            rows = self.db.delete_reservation_by_book(book_id=book_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="Reservation", field="book_id", value=book_id)
        return f"Deleted reservation for book {book_id}"

    def _validate_reservation_payload(self, reservation_payload):
        reservation = ReservationsDBModel(**reservation_payload)
        with self.db:
            rows = self.db.get_book_by_id(reservation.book_id)
            if not rows:
                raise ResourceNotFound(resource_type="Book", field="book_id", value=reservation.book_id)
            rows = self.db.get_user_by_id(reservation.user_id)
            if not rows:
                raise ResourceNotFound(resource_type="User", field="user_id", value=reservation.user_id)

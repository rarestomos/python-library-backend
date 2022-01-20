import random
import uuid
from datetime import date
from functools import wraps
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from library_backend import logger, Base
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.mock_data import books, get_users_list
from library_backend.models.database.reservations_db_model import ReservationsDBModel
from library_backend.models.database.users_db_model import UsersDBModel


def check_session():
    """
    Decorator function to check if the session has been initialized

    :return: callable
    :raises Exception
    """

    def check_session_wrapper(callable_func):
        @wraps(callable_func)
        def decor_inner(instance, *args, **kwargs):
            if not instance.session:
                raise AttributeError('No session. Please use context manager.')
            return callable_func(instance, *args, **kwargs)

        return decor_inner

    return check_session_wrapper


class SQLiteDatabaseConnection:

    def __init__(self):
        self.engine = create_engine("sqlite:///db.sqlite", echo=False)
        self.session = None
        self.connection_name = None

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    @check_session()
    def create_tables_if_not_exists(self):
        try:
            if not (self.engine.dialect.has_table(self.engine, UsersDBModel.__tablename__)
                    and self.engine.dialect.has_table(self.engine, BooksDBModel.__tablename__)
                    and self.engine.dialect.has_table(self.engine, ReservationsDBModel.__tablename__)):
                logger.info(f"Creating table {UsersDBModel.__tablename__}...")
                try:
                    Base.metadata.create_all(self.engine)
                except Exception as ex:
                    logger.error(ex)
                logger.info(f"Created table {UsersDBModel.__tablename__}...")
            else:
                logger.info(f"Table {UsersDBModel.__tablename__} already exists!")
        except SQLAlchemyError as e:
            logger.error(e, exc_info=True)
            raise

    @check_session()
    def add_user(self, user_model: UsersDBModel):
        user_id = str(uuid.uuid4())
        user_model.id = user_id
        self.session.add(user_model)

    @check_session()
    def add_book(self, book_model: BooksDBModel):
        book_id = str(uuid.uuid4())
        book_model.id = book_id
        self.session.add(book_model)

    @check_session()
    def add_reservation(self, reservation_model: ReservationsDBModel):
        self.session.add(reservation_model)

    @check_session()
    def get_all_users(self):
        return self.session.query(UsersDBModel).all()

    @check_session()
    def get_users_by_first_and_last_name(self, first_name, last_name):
        return self.session.query(UsersDBModel) \
            .filter(UsersDBModel.first_name == first_name,
                    UsersDBModel.last_name == last_name).all()

    @check_session()
    def get_user_by_id(self, user_id):
        return self.session.query(UsersDBModel) \
            .filter(UsersDBModel.id == user_id).one_or_none()

    @check_session()
    def get_user_by_email(self, email):
        return self.session.query(UsersDBModel).filter(UsersDBModel.email == email).one_or_none()

    @check_session()
    def get_all_books(self):
        return self.session.query(BooksDBModel).all()

    @check_session()
    def get_book_by_id(self, book_id):
        return self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).one_or_none()

    @check_session()
    def get_book_by_partial_name(self, name):
        return self.session.query(BooksDBModel).filter(BooksDBModel.name.ilike(f'%{name}%')).all()

    @check_session()
    def get_books_by_author(self, author):
        return self.session.query(BooksDBModel).filter(BooksDBModel.author == author).all()

    @check_session()
    def get_book_by_author_and_name(self, author, name):
        return self.session.query(BooksDBModel) \
            .filter(BooksDBModel.author == author,
                    BooksDBModel.name == name).one_or_none()

    @check_session()
    def get_books_by_partial_author_name(self, partial_name):
        return self.session.query(BooksDBModel) \
            .filter(BooksDBModel.author.ilike(f'%{partial_name}%')).all()

    @check_session()
    def get_reserved_books(self):
        result = self.session.query(UsersDBModel, BooksDBModel) \
            .join(ReservationsDBModel).join(BooksDBModel).all()
        return result

    @check_session()
    def get_full_reserved_books_info(self):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel).join(BooksDBModel).order_by(UsersDBModel.first_name).all()
        return result

    @check_session()
    def get_reserved_book_by_user_id_and_book_id(self, user_id, book_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel).join(BooksDBModel).filter(
            UsersDBModel.id == user_id).filter(BooksDBModel.id == book_id).one_or_none()
        return result

    @check_session()
    def update_user_by_values(self, user_id, user):
        updated_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).update(
            {"first_name": user.first_name,
             "last_name": user.last_name,
             "email": user.email})
        return updated_rows

    @check_session()
    def update_user(self, user_id, user):
        updated_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).update(user.serialize())
        return updated_rows

    @check_session()
    def update_book(self, book_id, book):
        updated_rows = self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).update(book.serialize())
        return updated_rows

    @check_session()
    def update_reservation(self, reservation):
        updated_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.book_id == reservation.book_id) \
            .filter(ReservationsDBModel.user_id == reservation.user_id).update(reservation.serialize())
        return updated_rows

    @check_session()
    def update_reservation_for_user(self, user_id, reservation):
        updated_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.user_id == user_id) \
            .update({"reservation_date": reservation.reservation_date,
                     "reservation_expiration_date": reservation.reservation_expiration_date})
        return updated_rows

    @check_session()
    def get_reserved_books_by_user_id(self, user_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel).join(BooksDBModel)\
            .filter(UsersDBModel.id == user_id).all()
        return result

    @check_session()
    def get_reservation_by_book_id(self, book_id):
        result = self.session.query(UsersDBModel, BooksDBModel, ReservationsDBModel) \
            .join(ReservationsDBModel).join(BooksDBModel) \
            .filter(BooksDBModel.id == book_id).all()
        return result

    @check_session()
    def delete_user_by_id(self, user_id):
        deleted_rows = self.session.query(UsersDBModel).filter(UsersDBModel.id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_book_by_id(self, book_id):
        deleted_rows = self.session.query(BooksDBModel).filter(BooksDBModel.id == book_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_user_and_book_id(self, user_id, book_id):
        deleted_rows = self.session.query(ReservationsDBModel)\
            .filter(ReservationsDBModel.book_id == book_id)\
            .filter(ReservationsDBModel.user_id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_user(self, user_id):
        deleted_rows = self.session.query(ReservationsDBModel)\
            .filter(ReservationsDBModel.user_id == user_id).delete()
        return deleted_rows

    @check_session()
    def delete_reservation_by_book(self, book_id):
        deleted_rows = self.session.query(ReservationsDBModel) \
            .filter(ReservationsDBModel.book_id == book_id).delete()
        return deleted_rows

    @check_session()
    def add_some_data_if_does_not_exist(self):
        user1 = UsersDBModel(email="adi.tamas@endava.com", first_name="Adrian", last_name="Tamas")
        user2 = UsersDBModel(email="ion.ionescu@endava.com", first_name="Ion", last_name="Ionescu")
        users = get_users_list()

        nr_of_entries = self.session.query(UsersDBModel).count()
        if nr_of_entries is 0:
            self.add_user(user1)
            self.add_user(user2)
            for user in users:
                self.add_user(user)

        nr_of_entries = self.session.query(BooksDBModel).count()
        if nr_of_entries is 0:
            for book in books:
                self.add_book(book)

        nr_of_entries = self.session.query(ReservationsDBModel).count()
        if nr_of_entries is 0:
            fake = Faker()
            start_date = date(year=2010, month=1, day=1)
            end_date = date(year=2019, month=1, day=1)
            for book in books:
                user = random.choice(users)
                fake_date = fake.date_between(start_date=start_date, end_date=end_date)
                reservation = ReservationsDBModel(book_id=book.id,
                                                  user_id=user.id,
                                                  reservation_expiration_date=None,
                                                  reservation_date=f"{fake_date}")
                self.add_reservation(reservation)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
            self.session.close()
            return False
        else:
            try:
                self.session.commit()
            except Exception as err:
                logger.error(f"Commit failed: {err}")
                self.session.rollback()
                self.session.close()
        self.session.close()




import json

from library_backend.database import SQLiteDatabaseConnection
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.reservations_db_model import ReservationsDBModel
from library_backend.models.database.users_db_model import UsersDBModel

db = SQLiteDatabaseConnection()
with db:
    # user1 = UsersDdb = SQLiteDatabaseConnection()
    # with db:BModel(user_email="adrian.tamas@endava.com", user_first_name="Adrian", last_name="Tamas")
    # db.add_user(user1)

    print("\n=========== User check ===========\n")
    users = db.get_all_users()
    print(f"All users: {users}")

    users1 = db.get_users_by_first_and_last_name(first_name="Adrian", last_name="Tamas")
    print(f"List of users by name {users1}")

    users2 = db.get_users_by_first_and_last_name(first_name="Adriana", last_name="Tamas")
    print(f"List non existing users {users2}")

    user = db.get_user_by_email(email="adi.tamas@endava.com")
    print(f"get user by email {user}")

    user_by_id = db.get_user_by_id(user.id)
    print(f"User by id {user_by_id}")

    print("\n=========== Books check ===========\n")

    all_books = db.get_all_books()
    print(f"All Books {all_books}")

    book_by_name = db.get_book_by_partial_name("Nightflyers")
    print(f"Book by exact name {book_by_name}")

    book_by_author = db.get_books_by_author("George R.R. Martin")
    print(f"Book by exact author name {book_by_author}")

    book_by_name_and_author = db.get_book_by_author_and_name(name="Nightflyers",
                                                             author="George R.R. Martin")
    print(f"Book by name and author: {book_by_name_and_author}")

    book_by_partial_name = db.get_books_by_partial_author_name("R.R.")
    print(f"Book by partial name {book_by_partial_name}")

    book_by_book_id = db.get_book_by_id(book_by_name[0].id)
    print(f"Book by id {book_by_book_id}")

    print("\n=========== Reservations check ===========\n")
    result = db.get_reserved_books()

    for user, book in result:
        print(f"User {user.first_name} {user.last_name} has reserved the book {book.name}"
              f" written by {book.author}")

    print("\n=========== Reservations check with dates ===========\n")
    result = db.get_full_reserved_books_info()
    for user, book, reservation in result:
        print(f"User {user.first_name} {user.last_name} has reserved the book {book.name}"
              f" written by {book.author} and was reserved on {reservation.reservation_date}")

    print("\n=========== Reservation by user_id and book_id ===========\n")
    user1, book1, reservation1 = result[0]
    user, book, reservation = db.get_reserved_book_by_user_id_and_book_id(user1.id, book1.id)
    print(f"User {user.first_name} {user.last_name} has reserved the book {book.name}"
          f" written by {book.author} and was reserved on {reservation.reservation_date}")

    print("\n=========== Update user ===========\n")
    user = db.get_user_by_email("ion.ionescu@endava.com")
    user.first_name = "Jon1"
    user.last_name = "Doe"

    row = db.update_user_by_values(user.id, user)
    print(f"Nr of edited rows: {row}")
    new_user = db.get_user_by_id(user.id)
    print(f"Edited User: {new_user}")

    print("\n=========== Serializers ===========\n")
    users1 = db.get_users_by_first_and_last_name(first_name="Adrian", last_name="Tamas")
    print(f"List of users by name {UsersDBModel.serialize_list(users1)}")

    book_by_name = db.get_book_by_partial_name("Nightflyers")
    print(f"Book by exact name {book_by_name}")

    user1, book1, reservation1 = result[0]
    user, book, reservation = db.get_reserved_book_by_user_id_and_book_id(user1.id, book1.id)
    print(f"User {user} has reserved the book {book}")

    print("\n=========== Update user ===========\n")
    user = db.get_user_by_email("ion.ionescu@endava.com")
    user.first_name = "Jon2"
    user.last_name = "Doe2"

    row = db.update_user(user.id, user)
    print(f"Nr of edited rows: {row}")
    new_user = db.get_user_by_id(user.id)
    print(f"Edited User: {new_user}")

    print("\n=========== Update book ===========\n")
    book_by_name = db.get_book_by_partial_name("Nightflyers")[0]
    row = db.update_book(book_by_name.id, book_by_name)
    print(f"Nr of edited rows: {row}")
    book_by_name = db.get_book_by_partial_name(book_by_name.name)
    print(f"Edited User: {book_by_name}")

    print("\n=========== Delete user ===========\n")
    user = UsersDBModel(email="a.tamas@endava.com", first_name="Adrian", last_name="Tamas")
    db.add_user(user)
    user = db.get_user_by_email(user.email)
    book_by_name = db.get_book_by_partial_name("Nightflyers")[0]
    reservation = ReservationsDBModel(user_id=user.id,
                                      book_id=book_by_name.id,
                                      reservation_date="soem",
                                      reservation_expiration_date=None)
    db.add_reservation(reservation)
    user, book, reservation = db.get_reserved_book_by_user_id_and_book_id(user.id, book_by_name.id)
    print(f"User {json.dumps(users[0].serialize())} has reserved the book {json.dumps(book.serialize())}")
    rows = db.delete_user_by_id(user.id)
    print(f"Nr of edited rows: {rows}")
    new_user = db.get_user_by_id(user.id)
    if not new_user:
        print("user not found")
    else:
        print(f"User: {new_user} was not deleted")

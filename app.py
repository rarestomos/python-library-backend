import logging

from flask import Flask, Response, request

from library_backend.api import UserApi, BookApi, ReservationApi
from library_backend.database import SQLiteDatabaseConnection

logger = logging.getLogger(__name__)

app = Flask("LibraryBackend")

CONTENT_TYPE = "application/json"


def app_response(api_response):
    return Response(response=api_response['body'], status=api_response['status_code'], content_type=CONTENT_TYPE)


@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json(force=True)
    user_api = UserApi()
    response = user_api.create_user(user)
    return app_response(response)


@app.route('/users', methods=['GET'])
def list_users():
    user_api = UserApi()
    response = user_api.list_users()
    return app_response(response)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_api = UserApi()
    response = user_api.delete_user(user_id)
    return app_response(response)


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    new_user = request.get_json(force=True)
    user_api = UserApi()
    response = user_api.update_user(user_id, new_user)
    return app_response(response)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_api = UserApi()
    response = user_api.get_user(user_id)
    return app_response(response)


@app.route('/books', methods=['GET'])
def get_books():
    book_api = BookApi()
    book_name = request.args.get("name")
    author_name = request.args.get("author")
    if book_name:
        response = book_api.get_books_by_name(book_name.strip("\"\'"))
    elif author_name:
        response = book_api.get_books_by_author(author_name.strip("\"\'"))
    else:
        response = book_api.get_books()
    return app_response(response)


@app.route('/books', methods=['POST'])
def create_book():
    book = request.get_json(force=True)
    book_api = BookApi()
    response = book_api.create_book(book)
    return app_response(response)


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book_api = BookApi()
    response = book_api.get_book(book_id)
    return app_response(response)


@app.route('/books/<book_id>', methods=['PUT'])
def edit_book(book_id):
    new_book = request.get_json(force=True)
    book_api = BookApi()
    response = book_api.update_book(book_id, new_book)
    return app_response(response)


@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_api = BookApi()
    response = book_api.delete_book(book_id)
    return app_response(response)


@app.route("/reservations", methods=["GET"])
def get_reservations():
    reservation_api = ReservationApi()
    response = reservation_api.get_reservations()
    return app_response(response)


@app.route("/reservations", methods=["POST"])
def add_reservation():
    reservation = request.get_json(force=True)
    reservation_api = ReservationApi()
    response = reservation_api.add_reservation(reservation)
    return app_response(response)


@app.route("/reservations/user/<user_id>", methods=["GET"])
def get_reservation_for_user(user_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_user_id(user_id)
    return app_response(response)


@app.route("/reservations/book/<book_id>", methods=["GET"])
def get_reservation_for_book(book_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_book_id(book_id)
    return app_response(response)


@app.route("/reservations/user/<user_id>/book/<book_id>", methods=["GET"])
def get_reservation_by_user_d_and_book_id(user_id, book_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_user_id_and_book_id(user_id=user_id, book_id=book_id)
    return app_response(response)


@app.route("/reservations/user/<user_id>/book/<book_id>", methods=["PUT"])
def update_reservation_for_user_and_book(user_id, book_id):
    reservation = request.get_json(force=True)
    reservation_api = ReservationApi()
    response = reservation_api.update_reservation(user_id=user_id,
                                                  book_id=book_id,
                                                  reservation_payload=reservation)
    return app_response(response)


@app.route("/reservations/user/<user_id>/book/<book_id>", methods=["DELETE"])
def delete_reservation_for_user_and_book(user_id, book_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_reservation(user_id, book_id)
    return app_response(response)


@app.route("/reservations/user/<user_id>", methods=["DELETE"])
def delete_all_reservations_for_user(user_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_all_reservations_for_users(user_id)
    return app_response(response)


@app.route("/reservations/book/<book_id>", methods=["DELETE"])
def delete_all_reservation_for_book(book_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_all_reservation_for_book(book_id)
    return app_response(response)


if __name__ == '__main__':
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    with db:
        db.add_some_data_if_does_not_exist()
    app.run(host="127.0.0.1", port=50000, debug=True)

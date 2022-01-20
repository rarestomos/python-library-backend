import logging

from flask import Blueprint, request

from library_backend.api import ReservationApi, app_response

logger = logging.getLogger(__name__)

reservations = Blueprint("reservations", __name__)


@reservations.route("/reservations", methods=["GET"])
def get_reservations():
    reservation_api = ReservationApi()
    response = reservation_api.get_reservations()
    return app_response(response)


@reservations.route("/reservations", methods=["POST"])
def add_reservation():
    reservation = request.get_json(force=True)
    reservation_api = ReservationApi()
    response = reservation_api.add_reservation(reservation)
    return app_response(response)


@reservations.route("/reservations/user/<user_id>", methods=["GET"])
def get_reservation_for_user(user_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_user_id(user_id)
    return app_response(response)


@reservations.route("/reservations/book/<book_id>", methods=["GET"])
def get_reservation_for_book(book_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_book_id(book_id)
    return app_response(response)


@reservations.route("/reservations/user/<user_id>/book/<book_id>", methods=["GET"])
def get_reservation_by_user_id_and_book_id(user_id, book_id):
    reservation_api = ReservationApi()
    response = reservation_api.get_reservation_by_user_id_and_book_id(user_id=user_id, book_id=book_id)
    return app_response(response)


@reservations.route("/reservations/user/<user_id>/book/<book_id>", methods=["PUT"])
def update_reservation_for_user_and_book(user_id, book_id):
    reservation = request.get_json(force=True)
    reservation_api = ReservationApi()
    response = reservation_api.update_reservation(user_id=user_id,
                                                  book_id=book_id,
                                                  reservation_payload=reservation)
    return app_response(response)


@reservations.route("/reservations/user/<user_id>/book/<book_id>", methods=["DELETE"])
def delete_reservation_for_user_and_book(user_id, book_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_reservation(user_id, book_id)
    return app_response(response)


@reservations.route("/reservations/user/<user_id>", methods=["DELETE"])
def delete_all_reservations_for_user(user_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_all_reservations_for_users(user_id)
    return app_response(response)


@reservations.route("/reservations/book/<book_id>", methods=["DELETE"])
def delete_all_reservations_for_book(book_id):
    reservation_api = ReservationApi()
    response = reservation_api.delete_all_reservation_for_book(book_id)
    return app_response(response)

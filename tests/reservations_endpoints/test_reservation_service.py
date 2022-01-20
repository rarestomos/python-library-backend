import copy

import mock
import pytest

from library_backend.exceptions import ResourceNotFound, ReservationAlreadyExists, ReservationIsInvalid, \
    DatabaseCommunicationIssue
from library_backend.service import (ReservationsDBModel,
                                     ReservationService,
                                     BooksDBModel,
                                     UsersDBModel)


class TestReservationService:

    def test_create_reservation_valid(self,
                                      mock_db_session,
                                      mock_reservation_payload,
                                      mock_book_resource,
                                      mock_user_resource,
                                      mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
            mock_db.side_effect = [None, (UsersDBModel(**mock_user_resource),
                                          BooksDBModel(**mock_book_resource),
                                          ReservationsDBModel(**mock_reservation_payload))]
            reservation_service = ReservationService()
            response = reservation_service.add_reservation(mock_reservation_payload)
        assert mock_reservation_resource == response

    def test_create_reservation_already_exists(self,
                                               mock_db_session,
                                               mock_reservation_payload,
                                               mock_book_resource,
                                               mock_user_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
            mock_db.return_value = (UsersDBModel(**mock_user_resource),
                                    BooksDBModel(**mock_book_resource),
                                    ReservationsDBModel(**mock_reservation_payload))
            reservation_service = ReservationService()
            with pytest.raises(ReservationAlreadyExists) as exc:
                response = reservation_service.add_reservation(mock_reservation_payload)
            assert f"Reservation for user: {mock_user_resource['id']}" \
                   f" and book: {mock_book_resource['id']} already exists" in exc.value.args[0]

    def test_create_reservation_not_created(self,
                                            mock_db_session,
                                            mock_reservation_payload,
                                            mock_book_resource,
                                            mock_user_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
            mock_db.return_value = None
            reservation_service = ReservationService()
            with pytest.raises(ResourceNotFound) as exc:
                response = reservation_service.add_reservation(mock_reservation_payload)
            assert f"Reservation with (user_id, book_id) =" \
                   f" ('{mock_user_resource['id']}', '{mock_book_resource['id']}') was not found" in exc.value.args[0]

    def test_list_all_reservations_valid(self,
                                         mock_db_session,
                                         mock_books_resource,
                                         mock_users_resource,
                                         mock_reservations_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_full_reserved_books_info") as mock_db:
            reservations = []
            mock_result = []
            for index, reservation in enumerate(mock_reservations_resource):
                mock_user = mock_users_resource[index]
                mock_book = mock_books_resource[index]
                mock_reservation = ReservationsDBModel(user_id=mock_user["id"],
                                                       book_id=mock_book["id"],
                                                       reservation_date=reservation["reservation_date"],
                                                       reservation_expiration_date=reservation["reservation_expiration_date"])
                reservations.append((UsersDBModel(**mock_user),
                                    BooksDBModel(**mock_book),
                                    mock_reservation))
                mock_result.append({"user": mock_user,
                                    "book": mock_book,
                                    "reservation_date":reservation["reservation_date"],
                                    "reservation_expiration_date":reservation["reservation_expiration_date"]})
            mock_db.return_value = reservations
            reservation_service = ReservationService()
            response = reservation_service.list_reservations()
        assert mock_result == response

    def test_get_reservation_by_user_and_book_id_valid(self,
                                                       mock_db_session,
                                                       mock_reservation_payload,
                                                       mock_book_resource,
                                                       mock_user_resource,
                                                       mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
            mock_db.return_value = (UsersDBModel(**mock_user_resource),
                                    BooksDBModel(**mock_book_resource),
                                    ReservationsDBModel(**mock_reservation_payload))
            reservation_service = ReservationService()
            response = reservation_service.get_reservation_by_user_id_and_book_id(book_id=mock_book_resource["id"],
                                                                                  user_id=mock_user_resource["id"])
        assert mock_reservation_resource == response

    def test_get_reservation_by_user_and_book_id_not_found(self,
                                                           mock_db_session,
                                                           mock_book_resource,
                                                           mock_user_resource,):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
            mock_db.return_value = None
            reservation_service = ReservationService()
            with pytest.raises(ResourceNotFound) as exc:
                response = reservation_service.get_reservation_by_user_id_and_book_id(book_id=mock_book_resource["id"],
                                                                                      user_id=mock_user_resource["id"])
        assert f"Reservation with (user_id, book_id) =" \
               f" ('{mock_user_resource['id']}', '{mock_book_resource['id']}') was not found" in exc.value.args[0]

    def test_get_reservation_by_user_id_valid(self,
                                              mock_db_session,
                                              mock_reservation_payload,
                                              mock_book_resource,
                                              mock_user_resource,
                                              mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_books_by_user_id") as mock_db:
            mock_db.return_value = [(UsersDBModel(**mock_user_resource),
                                     BooksDBModel(**mock_book_resource),
                                     ReservationsDBModel(**mock_reservation_payload))]
            reservation_service = ReservationService()
            response = reservation_service.get_reservation_by_user_id(user_id=mock_user_resource["id"])
        assert [mock_reservation_resource] == response

    def test_get_reservation_by_user_id_invalid(self,
                                                mock_db_session,
                                                mock_user_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reserved_books_by_user_id") as mock_db:
            mock_db.return_value = []
            reservation_service = ReservationService()
            response = reservation_service.get_reservation_by_user_id(user_id=mock_user_resource["id"])
        assert [] == response

    def test_get_reservation_by_book_id_valid(self,
                                              mock_db_session,
                                              mock_reservation_payload,
                                              mock_book_resource,
                                              mock_user_resource,
                                              mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reservation_by_book_id") as mock_db:
            mock_db.return_value = [(UsersDBModel(**mock_user_resource),
                                     BooksDBModel(**mock_book_resource),
                                     ReservationsDBModel(**mock_reservation_payload))]
            reservation_service = ReservationService()
            response = reservation_service.get_reservation_by_book_id(book_id=mock_book_resource["id"])
        assert [mock_reservation_resource] == response

    def test_get_reservation_by_book_id_invalid(self,
                                                mock_db_session,
                                                mock_book_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.get_reservation_by_book_id") as mock_db:
            mock_db.return_value = []
            reservation_service = ReservationService()
            response = reservation_service.get_reservation_by_book_id(book_id=mock_book_resource["id"])
        assert [] == response

    def test_delete_reservation_by_user_id_valid(self,
                                                 mock_db_session,
                                                 mock_user_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_user") as mock_db:
            mock_db.return_value = 5
            reservation_service = ReservationService()
            response = reservation_service.delete_reservations_for_user(user_id=mock_user_resource["id"])
        assert f"Deleted 5 reservations for users {mock_user_resource['id']}" == response

    def test_delete_reservation_by_user_id_invalid(self,
                                                   mock_db_session,
                                                   mock_user_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_user") as mock_db:
            mock_db.return_value = 0
            reservation_service = ReservationService()
            with pytest.raises(ResourceNotFound) as exc:
                response = reservation_service.delete_reservations_for_user(user_id=mock_user_resource["id"])
        assert f"Reservation with user_id = {mock_user_resource['id']} was not found" in exc.value.args[0]

    def test_delete_reservation_by_book_id_valid(self,
                                                 mock_db_session,
                                                 mock_book_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_book") as mock_db:
            mock_db.return_value = 1
            reservation_service = ReservationService()
            response = reservation_service.delete_reservation_for_book(book_id=mock_book_resource["id"])
        assert f"Deleted reservation for book {mock_book_resource['id']}" == response

    def test_delete_reservation_by_book_id_invalid(self,
                                                   mock_db_session,
                                                   mock_book_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_book") as mock_db:
            mock_db.return_value = 0
            reservation_service = ReservationService()
            with pytest.raises(ResourceNotFound) as exc:
                response = reservation_service.delete_reservation_for_book(book_id=mock_book_resource["id"])
        assert f"Reservation with book_id = {mock_book_resource['id']} was not found" in exc.value.args[0]

    def test_delete_reservation_by_user_and_book_id_valid(self,
                                                          mock_db_session,
                                                          mock_user_resource,
                                                          mock_book_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_user_and_book_id") as mock_db:
            mock_db.return_value = 1
            reservation_service = ReservationService()
            response = reservation_service.delete_reservation_by_user_and_book(user_id=mock_user_resource["id"],
                                                                               book_id=mock_book_resource["id"])
        assert f"Deleted reservation for users {mock_user_resource['id']}" \
               f" and book {mock_book_resource['id']}" == response

    def test_delete_reservation_by_user_and_book_id_invalid(self,
                                                            mock_db_session,
                                                            mock_user_resource,
                                                            mock_book_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.delete_reservation_by_user_and_book_id") as mock_db:
            mock_db.return_value = 0
            reservation_service = ReservationService()
            with pytest.raises(ResourceNotFound) as exc:
                response = reservation_service.delete_reservation_by_user_and_book(user_id=mock_user_resource["id"],
                                                                                   book_id=mock_book_resource["id"])
            assert f"Reservation with (user_id, book_id) =" \
                   f" ('{mock_user_resource['id']}', '{mock_book_resource['id']}') was not found" in exc.value.args[0]

    def test_update_reservation_valid(self,
                                      mock_db_session,
                                      mock_reservation_payload,
                                      mock_book_resource,
                                      mock_user_resource,
                                      mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.update_reservation", return_value=1):
            with mock.patch(
                    "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
                mock_db.return_value = (UsersDBModel(**mock_user_resource),
                                        BooksDBModel(**mock_book_resource),
                                        ReservationsDBModel(**mock_reservation_payload))
                reservation_service = ReservationService()
                response = reservation_service.update_reservation(user_id=mock_user_resource["id"],
                                                                  book_id=mock_book_resource["id"],
                                                                  reservation_payload=mock_reservation_payload)
        assert mock_reservation_resource == response

    def test_update_reservation_invalid_user_id(self,
                                                mock_db_session,
                                                mock_reservation_payload,
                                                mock_book_resource,
                                                mock_user_resource,
                                                mock_reservation_resource):
        reservation_service = ReservationService()
        with pytest.raises(ReservationIsInvalid) as exc:
            response = reservation_service.update_reservation(user_id=f"{mock_user_resource['id']}4",
                                                              book_id=mock_book_resource["id"],
                                                              reservation_payload=mock_reservation_payload)
        assert f'Reservation for user: ' \
               f'{ mock_reservation_resource["user"]["id"]}4 and ' \
               f'book: {mock_reservation_resource["book"]["id"]} is invalid' in exc.value.args[0]

    def test_update_reservation_invalid_book_id(self,
                                                mock_db_session,
                                                mock_reservation_payload,
                                                mock_book_resource,
                                                mock_user_resource,
                                                mock_reservation_resource):
        reservation_service = ReservationService()
        with pytest.raises(ReservationIsInvalid) as exc:
            response = reservation_service.update_reservation(user_id=mock_user_resource['id'],
                                                              book_id=f"{mock_book_resource['id']}4",
                                                              reservation_payload=mock_reservation_payload)
        assert f'Reservation for user: ' \
               f'{ mock_reservation_resource["user"]["id"]} and ' \
               f'book: {mock_reservation_resource["book"]["id"]}4 is invalid' in exc.value.args[0]

    def test_update_reservation_not_found(self,
                                          mock_db_session,
                                          mock_reservation_payload,
                                          mock_book_resource,
                                          mock_user_resource,
                                          mock_reservation_resource):
        with mock.patch(
                "library_backend.database.SQLiteDatabaseConnection.update_reservation", return_value=1):
            with mock.patch(
                    "library_backend.database.SQLiteDatabaseConnection.get_reserved_book_by_user_id_and_book_id") as mock_db:
                mock_db.return_value = None
                reservation_service = ReservationService()
                response = reservation_service.update_reservation(user_id=mock_user_resource["id"],
                                                                  book_id=mock_book_resource["id"],
                                                                  reservation_payload=mock_reservation_payload)
                assert response is None

    def test_update_reservation_db_update_fail(self,
                                               mock_db_session,
                                               mock_reservation_payload,
                                               mock_book_resource,
                                               mock_user_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.update_reservation", return_value=0):
            reservation_service = ReservationService()
            with pytest.raises(DatabaseCommunicationIssue) as exc:
                response = reservation_service.update_reservation(user_id=mock_user_resource["id"],
                                                                  book_id=mock_book_resource["id"],
                                                                  reservation_payload=mock_reservation_payload)
            assert f"There was an error performing the update reservation" in exc.value.args[0]

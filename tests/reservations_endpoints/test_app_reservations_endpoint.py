import json

from unittest.mock import patch

import app
from library_backend.exceptions import ResourceNotFound, ReservationIsInvalid, DatabaseCommunicationIssue


class TestLibraryBackendAppReservationsEndpoints:

    def test_reservation_create_valid_all_values(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '200' == response.status
            assert mock_reservation_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_create_valid_required_only(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            del mock_reservation_payload["reservation_expiration_date"]
            mock_reservation_resource["reservation_expiration_date"] = None
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '200' == response.status
            assert mock_reservation_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_create_user_id_required(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            del mock_reservation_payload["user_id"]
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'user_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_user_id_required_when_empty(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["user_id"] = ""
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'user_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_user_id_required_when_none(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["user_id"] = None
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'user_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_book_id_required(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            del mock_reservation_payload["book_id"]
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'book_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_book_id_required_when_empty(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["book_id"] = ""
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'book_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_book_id_required_when_none(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["book_id"] = None
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'book_id\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_reservation_date_required(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            del mock_reservation_payload["reservation_date"]
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'reservation_date\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_reservation_date_required_when_empty(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["reservation_date"] = ""
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'reservation_date\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_create_reservation_date_required_when_none(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.add_reservation') as test_mock:
            mock_reservation_payload["reservation_date"] = None
            test_mock.return_value = mock_reservation_resource
            with app.app.test_client() as client:
                response = client.post('/reservations', json=mock_reservation_payload)
            assert '400' == response.status
            assert '"\'reservation_date\' is required"' == response.get_data().decode('utf-8')

    def test_reservation_get_by_user_id_and_book_id_valid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_user_id_and_book_id') as test_mock:
            test_mock.return_value = mock_reservation_resource
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '200' == response.status
            assert mock_reservation_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_get_by_invalid_user_id_and_valid_book_id(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_user_id_and_book_id') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="reservation",
                                                     field="user_id and book_id",
                                                     value=f"456 and {mock_reservation_resource['book']['id']}")
            endpoint_url = f'/reservations/user/456/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '400' == response.status
            assert '"reservation with user_id and book_id = 456 and 123 was not found"' == response.get_data().decode('utf-8')

    def test_reservation_get_by_valid_user_id_and_invalid_book_id(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_user_id_and_book_id') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="reservation",
                                                     field="user_id and book_id",
                                                     value=f"{mock_reservation_resource['user']['id']} and 456")
            endpoint_url = f"/reservations/user/{mock_reservation_resource['user']['id']}/book/456"
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '400' == response.status
            assert '"reservation with user_id and book_id = 123 and 456 was not found"' == response.get_data().decode('utf-8')

    def test_reservation_get_by_book_id_valid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_book_id') as test_mock:
            test_mock.return_value = [mock_reservation_resource]
            endpoint_url = f'/reservations/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '200' == response.status
            assert [mock_reservation_resource] == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_get_by_book_id_invalid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_book_id') as test_mock:
            test_mock.return_value = []
            endpoint_url = f'/reservations/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '200' == response.status
            assert [] == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_get_by_user_id_valid(self, mock_reservations_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_user_id') as test_mock:
            test_mock.return_value = mock_reservations_resource
            endpoint_url = f"/reservations/user/{mock_reservations_resource[0]['user']['id']}"
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '200' == response.status
            assert mock_reservations_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_get_by_user_id_invalid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.get_reservation_by_user_id') as test_mock:
            test_mock.return_value = []
            endpoint_url = f"/reservations/user/{mock_reservation_resource['user']['id']}"
            with app.app.test_client() as client:
                response = client.get(endpoint_url)
            assert '200' == response.status
            assert [] == json.loads(response.get_data().decode('utf-8'))

    def test_reservations_get_valid(self, mock_reservations_resource):
        with patch('library_backend.service.ReservationService.list_reservations') as test_mock:
            test_mock.return_value = mock_reservations_resource
            with app.app.test_client() as client:
                response = client.get(f'/reservations')
            assert '200' == response.status
            assert mock_reservations_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_delete_by_user_and_book_id_valid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservation_by_user_and_book') as test_mock:
            test_mock.return_value = f"Deleted reservation for users {mock_reservation_resource['user']['id']}" \
                f" and book {mock_reservation_resource['book']['id']}"
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '200' == response.status
            assert f"Deleted reservation for users {mock_reservation_resource['user']['id']} " \
                   f"and book {mock_reservation_resource['book']['id']}" == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_delete_by_user_and_book_id_invalid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservation_by_user_and_book') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="reservation",
                                                     field="user_id and book_id",
                                                     value=f"{mock_reservation_resource['user']['id']}"
                                                           f" and {mock_reservation_resource['book']['id']}")
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '400' == response.status
            assert '"reservation with user_id and book_id = 123 and 123 was not found"' == response.get_data().decode('utf-8')

    def test_reservation_delete_by_user_id_valid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservations_for_user') as test_mock:
            test_mock.return_value = f'Deleted 3 reservations for users ' \
                   f'{mock_reservation_resource["user"]["id"]}'
            endpoint_url = f"/reservations/user/{mock_reservation_resource['user']['id']}"
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '200' == response.status
            assert f'Deleted 3 reservations for users ' \
                   f'{mock_reservation_resource["user"]["id"]}' == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_delete_by_user_id_invalid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservations_for_user') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="Reservation",
                                                     field="user_id",
                                                     value=f"{mock_reservation_resource['user']['id']}")
            endpoint_url = f"/reservations/user/{mock_reservation_resource['user']['id']}"
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '400' == response.status
            assert f'Reservation with user_id = {mock_reservation_resource["user"]["id"]} was not found'\
                   == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_delete_by_book_id_valid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservation_for_book') as test_mock:
            test_mock.return_value = f'Deleted reservation for book ' \
                   f'{mock_reservation_resource["book"]["id"]}'
            endpoint_url = f"/reservations/book/{mock_reservation_resource['book']['id']}"
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '200' == response.status
            assert f'Deleted reservation for book ' \
                   f'{mock_reservation_resource["book"]["id"]}' == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_delete_by_book_id_invalid(self, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.delete_reservation_for_book') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="Reservation",
                                                     field="book_id",
                                                     value=f"{mock_reservation_resource['book']['id']}")
            endpoint_url = f"/reservations/book/{mock_reservation_resource['book']['id']}"
            with app.app.test_client() as client:
                response = client.delete(endpoint_url)
            assert '400' == response.status
            assert f'Reservation with book_id = {mock_reservation_resource["book"]["id"]} was not found'\
                   == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_update_valid(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.update_reservation') as test_mock:
            test_mock.return_value = mock_reservation_resource
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.put(endpoint_url, json=mock_reservation_payload)
            assert '200' == response.status
            assert mock_reservation_resource == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_update_invalid_reservation(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.update_reservation') as test_mock:
            test_mock.side_effect = ReservationIsInvalid({"user_id": mock_reservation_resource["user"]["id"],
                                                          "book_id": mock_reservation_resource["book"]["id"]})
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.put(endpoint_url, json=mock_reservation_payload)
            assert '400' == response.status
            assert f'Reservation for user: ' \
                   f'{ mock_reservation_resource["user"]["id"]} and ' \
                   f'book: {mock_reservation_resource["book"]["id"]} is invalid' == json.loads(response.get_data().decode('utf-8'))

    def test_reservation_update_unable_to_update(self, mock_reservation_payload, mock_reservation_resource):
        with patch('library_backend.service.ReservationService.update_reservation') as test_mock:
            test_mock.side_effect = DatabaseCommunicationIssue("update reservation")
            endpoint_url = f'/reservations/user/{mock_reservation_resource["user"]["id"]}' \
                f'/book/{mock_reservation_resource["book"]["id"]}'
            with app.app.test_client() as client:
                response = client.put(endpoint_url, json=mock_reservation_payload)
            assert '500' == response.status
            assert f'There was an error performing the update reservation' == json.loads(response.get_data().decode('utf-8'))

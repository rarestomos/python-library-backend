import json
from copy import deepcopy
from unittest.mock import patch

import app
from library_backend.exceptions import ResourceNotFound, InvalidFieldException


class TestLibraryBackendAppUserEndpoints:

    def test_user_create_valid(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            with app.app.test_client() as client:
                response = client.post('/users', json=mock_user_payload)
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_user_create_first_name_required(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            del payload["first_name"]
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'first_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_first_name_required_when_empty(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["first_name"] = ""
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'first_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_first_name_required_when_none(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["first_name"] = None
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'first_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_last_name_required(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            del payload["last_name"]
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'last_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_last_name_required_when_empty(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["last_name"] = ""
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'last_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_last_name_required_when_none(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["last_name"] = None
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'last_name\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_email_required(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            del payload["email"]
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'email\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_email_required_when_empty(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["email"] = ""
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'email\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_email_required_when_none(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["email"] = None
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'email\' is required"' == response.get_data().decode('utf-8')

    def test_user_create_email_invalid(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = mock_user_payload
            payload["email"] = "abc"
            with app.app.test_client() as client:
                response = client.post('/users', json=payload)
            assert '400' == response.status
            assert '"\'email\' is invalid"' == response.get_data().decode('utf-8')

    def test_get_user_valid(self, mock_user_resource):
        with patch('library_backend.service.UserService.get_user') as test_mock:
            test_mock.return_value = mock_user_resource
            with app.app.test_client() as client:
                response = client.get(f'/users/{mock_user_resource["id"]}')
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_get_user_invalid_id(self, mock_user_resource):
        with patch('library_backend.service.UserService.get_user') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="User", field="user_id", value=mock_user_resource["id"])
            with app.app.test_client() as client:
                response = client.get(f'/users/{mock_user_resource["id"]}')
            assert '400' == response.status
            assert f'"User with user_id = {mock_user_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_list_user_valid(self, mock_users_resource):
        with patch('library_backend.service.UserService.list_users') as test_mock:
            test_mock.return_value = mock_users_resource
            with app.app.test_client() as client:
                response = client.get(f'/users')
            assert '200' == response.status
            assert mock_users_resource == json.loads(response.get_data().decode('utf-8'))

    def test_delete_user_valid(self, mock_user_resource):
        with patch('library_backend.service.UserService.delete_user') as test_mock:
            test_mock.return_value = f"Successfully deleted user {mock_user_resource['id']}"
            with app.app.test_client() as client:
                response = client.delete(f'/users/{mock_user_resource["id"]}')
            assert '200' == response.status
            assert f"Successfully deleted user {mock_user_resource['id']}" in response.get_data().decode('utf-8')

    def test_delete_user_invalid_id(self, mock_user_resource):
        with patch('library_backend.service.UserService.delete_user') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="User", field="user_id", value=mock_user_resource["id"])
            with app.app.test_client() as client:
                response = client.delete(f'/users/{mock_user_resource["id"]}')
            assert '400' == response.status
            assert f'"User with user_id = {mock_user_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_edit_user_valid(self, mock_user_resource):
        with patch('library_backend.service.UserService.update_user') as test_mock:
            test_mock.return_value = mock_user_resource
            with app.app.test_client() as client:
                response = client.put(f'/users/{mock_user_resource["id"]}', json=mock_user_resource)
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_edit_user_ignore_id(self, mock_user_resource):
        with patch('library_backend.service.UserService.update_user') as test_mock:
            test_mock.return_value = mock_user_resource
            payload = deepcopy(mock_user_resource)
            payload["id"] = "987"
            with app.app.test_client() as client:
                response = client.put(f'/users/{mock_user_resource["id"]}', json=mock_user_resource)
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_edit_user_invalid_id(self, mock_user_resource):
        with patch('library_backend.service.UserService.update_user') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="User", field="user_id", value=mock_user_resource["id"])
            with app.app.test_client() as client:
                response = client.put(f'/users/{mock_user_resource["id"]}', json=mock_user_resource)
            assert '400' == response.status
            assert f'"User with user_id = {mock_user_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_edit_user_invalid_change_email(self, mock_user_resource):
        with patch('library_backend.service.UserService.update_user') as test_mock:
            test_mock.side_effect = InvalidFieldException("email")
            payload = deepcopy(mock_user_resource)
            payload["email"] = "alternate@email.com"
            with app.app.test_client() as client:
                response = client.put(f'/users/{mock_user_resource["id"]}', json=mock_user_resource)
            assert '400' == response.status
            assert f'"\'email\' is invalid"' == response.get_data().decode('utf-8')

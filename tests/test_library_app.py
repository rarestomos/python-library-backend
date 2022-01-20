import copy
import json

from unittest.mock import patch

import app


class TestLibraryBackendApp:

    def test_user_create_valid(self, mock_user_payload, mock_user_resource):
        with patch('library_backend.service.UserService.create_user') as test_mock:
            test_mock.return_value = mock_user_resource
            with app.app.test_request_context('/users', method="POST",
                                              json=mock_user_payload):
                response = app.create_user()
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_get_user_valid(self, mock_user_resource):
        with patch('library_backend.service.UserService.get_user') as test_mock:
            test_mock.return_value = mock_user_resource
            with app.app.test_request_context(f'/users/{mock_user_resource["id"]}', method="GET"):
                response = app.get_user(mock_user_resource["id"])
            assert '200' == response.status
            assert mock_user_resource == json.loads(response.get_data().decode('utf-8'))

    def test_delete_user_valid(self, mock_user_resource):
        with patch('library_backend.service.UserService.delete_user') as test_mock:
            test_mock.return_value = f"Successfully deleted user {mock_user_resource['id']}"
            with app.app.test_request_context(f'/users/{mock_user_resource["id"]}', method="DELETE"):
                response = app.delete_user(mock_user_resource["id"])
            assert '200' == response.status
            assert f"Successfully deleted user {mock_user_resource['id']}" in response.get_data().decode('utf-8')

import copy

import mock
import pytest

from library_backend.exceptions import UserAlreadyExists, ResourceNotFound, InvalidFieldException
from library_backend.service import UserService, UsersDBModel


class TestUserService:

    def test_create_user_valid(self, mock_db_session, mock_user_payload, mock_user_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_email") as mock_db_get:
            mock_db_get.side_effect = [None, UsersDBModel(**mock_user_resource)]
            user_service = UserService()
            response = user_service.create_user(mock_user_payload)
        assert mock_user_resource == response

    def test_create_user_with_existing_email(self, mock_db_session, mock_user_payload, mock_user_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_email") as mock_db_get:
            mock_db_get.return_value = UsersDBModel(**mock_user_resource)
            user_service = UserService()
            with pytest.raises(UserAlreadyExists) as exc:
                response = user_service.create_user(mock_user_payload)
        assert f"User with email: {mock_user_payload['email']} already exists" in exc.value.args[0]

    def test_get_all_users(self, mock_db_session, mock_users_resource):
        mock_users = [UsersDBModel(**user) for user in mock_users_resource]
        mock_db_session.query(mock.ANY).all.return_value = mock_users
        user_service = UserService()
        response = user_service.list_users()
        assert mock_users_resource == response

    def test_get_empty_users_list(self, mock_db_session):
        mock_db_session.query(mock.ANY).all.return_value = []
        user_service = UserService()
        response = user_service.list_users()
        assert [] == response

    def test_get_user_by_id(self, mock_db_session, mock_user_resource):
        mock_db_session.query(mock.ANY).filter(mock.ANY).one_or_none.return_value = UsersDBModel(**mock_user_resource)
        user_service = UserService()
        response = user_service.get_user("123")
        assert mock_user_resource == response

    def test_get_user_by_invalid_id(self, mock_db_session):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_id") as mock_db_get:
            mock_db_get.return_value = None
            user_service = UserService()
            with pytest.raises(ResourceNotFound) as exc:
                response = user_service.get_user("123")
        assert "User with id = 123 was not found" in exc.value.args[0]

    def test_delete_user_by_id(self, mock_db_session):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.delete_user_by_id") as mock_db_del:
            mock_db_del.return_value = 1
            user_service = UserService()
            response = user_service.delete_user("123")
        assert "Successfully deleted user 123" == response

    def test_delete_user_by_invalid_id(self, mock_db_session):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.delete_user_by_id") as mock_db_del:
            mock_db_del.return_value = 0
            user_service = UserService()
            with pytest.raises(ResourceNotFound) as exc:
                response = user_service.delete_user("123")
            assert "User with id = 123 was not found" in exc.value.args[0]

    def test_edit_user_valid(self, mock_db_session, mock_user_resource):
        edited_user_payload = copy.deepcopy(mock_user_resource)
        edited_user_payload["first_name"] = "Jane"
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_id") as mock_db_get:
            mock_db_get.side_effect = [UsersDBModel(**mock_user_resource), UsersDBModel(**edited_user_payload)]
            user_service = UserService()
            response = user_service.update_user(mock_user_resource["id"], edited_user_payload)
        assert edited_user_payload == response

    def test_edit_user_invalid_id(self, mock_db_session, mock_user_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_id") as mock_db_get:
            mock_db_get.return_value = None
            user_service = UserService()
            with pytest.raises(ResourceNotFound) as exc:
                response = user_service.update_user(mock_user_resource["id"], mock_user_resource)
            assert f"User with id = {mock_user_resource['id']} was not found" in exc.value.args[0]

    def test_edit_user_invalid_email_change(self, mock_db_session, mock_user_resource):
        edited_user_payload = copy.deepcopy(mock_user_resource)
        edited_user_payload["email"] = "Jane@email.com"
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_user_by_id") as mock_db_get:
            mock_db_get.return_value = UsersDBModel(**mock_user_resource)
            user_service = UserService()
            with pytest.raises(InvalidFieldException) as exc:
                response = user_service.update_user(mock_user_resource["id"], edited_user_payload)
            assert f"'email' is invalid" in exc.value.args[0]

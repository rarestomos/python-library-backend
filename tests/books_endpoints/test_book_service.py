import copy

import mock
import pytest

from library_backend.exceptions import BookAlreadyExists, ResourceNotFound
from library_backend.service import BookService, BooksDBModel


class TestBookService:

    def test_create_book_valid(self, mock_db_session, mock_book_payload, mock_book_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_author_and_name") as mock_db_get:
            mock_db_get.side_effect = [None, BooksDBModel(**mock_book_resource)]
            book_service = BookService()
            response = book_service.create_book(mock_book_payload)
        assert mock_book_resource == response

    def test_create_book_already_exists(self, mock_db_session, mock_book_payload, mock_book_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_author_and_name") as mock_db_get:
            mock_db_get.return_value = BooksDBModel(**mock_book_resource)
            book_service = BookService()
            with pytest.raises(BookAlreadyExists) as exc:
                response = book_service.create_book(mock_book_payload)
        assert f"Book with name: {mock_book_resource['name']} " \
               f"writen by author: {mock_book_resource['author']} already exists"\
               in exc.value.args[0]

    def test_list_all_books(self, mock_db_session, mock_books_resource):
        mock_books = [BooksDBModel(**book) for book in mock_books_resource]
        mock_db_session.query(mock.ANY).all.return_value = mock_books
        book_service = BookService()
        response = book_service.list_books()
        assert mock_books_resource == response

    def test_list_all_books_empty_list(self, mock_db_session):
        mock_db_session.query(mock.ANY).all.return_value = []
        book_service = BookService()
        response = book_service.list_books()
        assert [] == response

    def test_get_book_by_id(self, mock_db_session, mock_book_resource):
        mock_db_session.query(mock.ANY).filter(mock.ANY).one_or_none.return_value = BooksDBModel(**mock_book_resource)
        book_service = BookService()
        response = book_service.get_book(mock_book_resource["id"])
        assert mock_book_resource == response

    def test_get_book_by_invalid_id(self, mock_db_session):
        mock_db_session.query(mock.ANY).filter(mock.ANY).one_or_none.return_value = None
        book_service = BookService()
        with pytest.raises(ResourceNotFound) as exc:
            response = book_service.get_book("123")
        assert "Book with id = 123 was not found" in exc.value.args[0]

    def test_delete_book_by_valid_id(self, mock_db_session, mock_book_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.delete_book_by_id") as mock_db_delete:
            mock_db_delete.return_value = 1
            book_service = BookService()
            response = book_service.delete_book(mock_book_resource["id"])
        assert "Successfully deleted book 123" == response

    def test_delete_book_by_invalid_id(self, mock_db_session, mock_book_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.delete_book_by_id") as mock_db_delete:
            mock_db_delete.return_value = 0
            book_service = BookService()
            with pytest.raises(ResourceNotFound) as exc:
                response = book_service.delete_book(mock_book_resource["id"])
            assert "Book with id = 123 was not found" in exc.value.args[0]

    def test_edit_book_valid(self, mock_db_session, mock_book_resource):
        edit_book_payload = copy.deepcopy(mock_book_resource)
        edit_book_payload["name"] = "Edited book title"
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_id") as mock_db_get:
            mock_db_get.side_effect = [BooksDBModel(**mock_book_resource), BooksDBModel(**edit_book_payload)]
            book_service = BookService()
            response = book_service.edit_book(edit_book_payload["id"], edit_book_payload)
        assert edit_book_payload == response

    def test_edit_book_invalid_id(self, mock_db_session, mock_book_resource):
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_id") as mock_db_get:
            mock_db_get.return_value = None
            book_service = BookService()
            with pytest.raises(ResourceNotFound) as exc:
                response = book_service.edit_book(mock_book_resource["id"], mock_book_resource)
            assert f"Book with id = {mock_book_resource['id']} was not found" in exc.value.args[0]

    def test_edit_book_invalid_book_already_exists(self, mock_db_session, mock_book_resource):
        edit_book_payload = copy.deepcopy(mock_book_resource)
        edit_book_payload["name"] = "Edited book title"
        edit_book_payload["id"] = "456"
        with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_id", return_value=BooksDBModel(**mock_book_resource)):
            with mock.patch("library_backend.database.SQLiteDatabaseConnection.get_book_by_author_and_name") as mock_db_get:
                mock_db_get.return_value = BooksDBModel(**edit_book_payload)
                book_service = BookService()
                with pytest.raises(BookAlreadyExists) as exc:
                    response = book_service.edit_book(mock_book_resource["id"], mock_book_resource)
                assert f"Book with name: {mock_book_resource['name']} writen by author: {mock_book_resource['author']} already exists" in exc.value.args[0]

import json

from unittest.mock import patch

import app
from library_backend.exceptions import ResourceNotFound, BookAlreadyExists


class TestLibraryBackendAppBookEndpoints:

    def test_book_create_valid_all_values(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
                # response = app.books.create_book()
            assert '200' == response.status
            assert mock_book_resource == json.loads(response.get_data().decode('utf-8'))

    def test_book_create_valid_mandatory_values(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            mock_book_resource["description"] = None
            mock_book_resource["cover"] = None
            test_mock.return_value = mock_book_resource
            del mock_book_payload["description"]
            del mock_book_payload["cover"]
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '200' == response.status
            assert mock_book_resource == json.loads(response.get_data().decode('utf-8'))

    def test_book_create_name_required(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            del mock_book_payload["name"]
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'name\' is required"' == response.get_data().decode('utf-8')

    def test_book_create_author_required(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            del mock_book_payload["author"]
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'author\' is required"' == response.get_data().decode('utf-8')

    def test_book_create_name_required_when_empty(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            mock_book_payload["name"] = ""
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'name\' is required"' == response.get_data().decode('utf-8')

    def test_book_create_author_required_when_empty(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            mock_book_payload["author"] = ""
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'author\' is required"' == response.get_data().decode('utf-8')

    def test_book_create_name_required_when_none(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            mock_book_payload["name"] = None
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'name\' is required"' == response.get_data().decode('utf-8')

    def test_book_create_author_required_when_none(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            mock_book_payload["author"] = None
            with app.app.test_client() as client:
                response = client.post("/books", json=mock_book_payload)
            assert '400' == response.status
            assert '"\'author\' is required"' == response.get_data().decode('utf-8')

    def test_get_book_valid(self, mock_book_resource):
        with patch('library_backend.service.BookService.get_book') as test_mock:
            test_mock.return_value = mock_book_resource
            with app.app.test_client() as client:
                response = client.get(f'/books/{mock_book_resource["id"]}')
            assert '200' == response.status
            assert mock_book_resource == json.loads(response.get_data().decode('utf-8'))

    def test_get_book_invalid_id(self, mock_book_resource):
        with patch('library_backend.service.BookService.get_book') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="Book", field="book_id", value=mock_book_resource["id"])
            with app.app.test_client() as client:
                response = client.get(f'/books/{mock_book_resource["id"]}')
            assert '400' == response.status
            assert f'"Book with book_id = {mock_book_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_list_book_valid(self, mock_books_resource):
        with patch('library_backend.service.BookService.list_books') as test_mock:
            test_mock.return_value = mock_books_resource
            with app.app.test_client() as client:
                response = client.get('/books')
            assert '200' == response.status
            assert mock_books_resource == json.loads(response.get_data().decode('utf-8'))

    def test_delete_book_valid(self, mock_book_resource):
        with patch('library_backend.service.BookService.delete_book') as test_mock:
            test_mock.return_value = f"Successfully deleted book {mock_book_resource['id']}"
            with app.app.test_client() as client:
                response = client.delete(f'/books/{mock_book_resource["id"]}')
            assert '200' == response.status
            assert f"Successfully deleted book {mock_book_resource['id']}" == json.loads(response.get_data().decode('utf-8'))

    def test_delete_book_invalid_id(self, mock_book_resource):
        with patch('library_backend.service.BookService.delete_book') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="Book", field="book_id", value=mock_book_resource["id"])
            with app.app.test_client() as client:
                response = client.delete(f'/books/{mock_book_resource["id"]}')
            assert '400' == response.status
            assert f'"Book with book_id = {mock_book_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_edit_book_valid(self, mock_book_resource):
        with patch('library_backend.service.BookService.edit_book') as test_mock:
            test_mock.return_value = mock_book_resource
            with app.app.test_client() as client:
                response = client.put(f'/books/{mock_book_resource["id"]}', json=mock_book_resource)
            assert '200' == response.status
            assert mock_book_resource == json.loads(response.get_data().decode('utf-8'))

    def test_edit_book_invalid_id(self, mock_book_resource):
        with patch('library_backend.service.BookService.edit_book') as test_mock:
            test_mock.side_effect = ResourceNotFound(resource_type="Book", field="book_id", value=mock_book_resource["id"])
            with app.app.test_client() as client:
                response = client.put(f'/books/{mock_book_resource["id"]}', json=mock_book_resource)
            assert '400' == response.status
            assert f'"Book with book_id = {mock_book_resource["id"]} was not found"' == response.get_data().decode('utf-8')

    def test_edit_book_invalid_already_exists(self, mock_book_resource):
        with patch('library_backend.service.BookService.edit_book') as test_mock:
            test_mock.side_effect = BookAlreadyExists(mock_book_resource)
            with app.app.test_client() as client:
                response = client.put(f'/books/{mock_book_resource["id"]}', json=mock_book_resource)
            assert '400' == response.status
            assert f'"Book with name: {mock_book_resource["name"]} ' \
                   f'writen by author: {mock_book_resource["author"]} already exists"'\
                   == response.get_data().decode('utf-8')

from unittest import mock

import pytest
import app


@pytest.fixture()
def mock_user_payload():
    yield {
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }


@pytest.fixture()
def mock_user_resource():
    yield {
        "id": "123",
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }


@pytest.fixture()
def mock_users_resource():
    yield [{
        "id": "123",
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }, {
        "id": "456",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "janesmith@email.com"
    }]


@pytest.fixture()
def mock_book_payload():
    yield {
        "name": "My test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }


@pytest.fixture()
def mock_book_resource():
    yield {
        "id": "123",
        "name": "My test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }


@pytest.fixture()
def mock_books_resource():
    yield [{
        "id": "123",
        "name": "My test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }, {
        "id": "456",
        "name": "My second test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }]


@pytest.fixture()
def mock_reservation_payload():
    yield {
        "book_id": "123",
        "user_id": "123",
        "reservation_date": "2019-01-01",
        "reservation_expiration_date": "2019-12-12"
    }


@pytest.fixture()
def mock_reservation_resource():
    yield {
        "user": {
            "id": "123",
            "first_name": "John",
            "last_name": "Smith",
            "email": "jhonsmith@email.com"
        },
        "book": {
            "id": "123",
            "name": "My test book",
            "author": "Unknown Author",
            "description": "A test book created for unit tests",
            "cover": "https://test.com/cover.jpg"
        },
        "reservation_date": "2019-01-01",
        "reservation_expiration_date": "2019-12-12"
    }


@pytest.fixture()
def mock_reservations_resource():
    yield [{
        "user": {
            "id": "123",
            "first_name": "John",
            "last_name": "Smith",
            "email": "jhonsmith@email.com"
        },
        "book": {
            "id": "123",
            "name": "My test book",
            "author": "Unknown Author",
            "description": "A test book created for unit tests",
            "cover": "https://test.com/cover.jpg"
        },
        "reservation_date": "2019-01-01",
        "reservation_expiration_date": "2019-12-12"
    }, {
        "user": {
            "id": "123",
            "first_name": "John",
            "last_name": "Smith",
            "email": "jhonsmith@email.com"
        },
        "book": {
            "id": "456",
            "name": "My test book 2",
            "author": "Unknown Author",
            "description": "A test book created for unit tests",
            "cover": "https://test.com/cover.jpg"
        },
        "reservation_date": "2019-06-06",
        "reservation_expiration_date": "2019-12-12"
    }]


@pytest.fixture(scope="session")
def mock_db_session():
    with mock.patch('library_backend.database.create_engine'):
        with mock.patch('library_backend.database.sessionmaker') as sessionmaker_mock:
            session = sessionmaker_mock()()
            yield session

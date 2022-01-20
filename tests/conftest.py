import pytest


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

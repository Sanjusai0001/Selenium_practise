import pytest
import requests
from ..source import service as service
import unittest.mock as mock


# Mocking


@mock.patch("Pytest_Module.source.service.get_user_from_db")
def test_get_user_from_db_mocked(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Ryan"
    user_name = service.get_user_from_db(3)

    assert user_name == "Mocked Ryan"


@mock.patch("Pytest_Module.source.service.get_user_from_db")
def test_get_user_from_db_original(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Kimiko"
    user_name = service.get_user_from_db(10)

    assert user_name == "Kimiko"


# using requests

@mock.patch("requests.get")
def test_get_users_mocked(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": "1", "name": "Kimiko"}]
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == [{"id": "1", "name": "Kimiko"}]



@mock.patch("requests.get")
def test_get_users_errorl(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
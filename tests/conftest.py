import httpx
import pytest
from fastapi.testclient import TestClient

from fastapi.testclient import TestClient
from main import app
from schemas.user_schema import User
from services import service
client = TestClient(app)



# @pytest.fixture
# def client():
#     return TestClient(app)
#
#
# def test_get(client: TestClient):
#     response = client.get("/api/users")
#     assert response.status_code == 200



def test_get_users():
    # Получаем список пользователей через API
    response = client.get("/api/users")
    assert response.status_code == 200
    users = response.json()

    # Получаем список пользователей напрямую из сервиса
    expected_users = service.get_users()

    # Проверяем, что списки пользователей совпадают
    assert len(users) == len(expected_users)
    for i in range(len(users)):
        assert users[i]["id"] == expected_users[i].id
        assert users[i]["email"] == expected_users[i].email
        assert users[i]["username"] == expected_users[i].username
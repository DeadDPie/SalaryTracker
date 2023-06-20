from fastapi.testclient import TestClient
from .variables import Vars as var
from main import app

client = TestClient(app)

def test_get_users():
    """
    Получение сотрудников
    """
    response = client.get("/api/users")
    assert response.status_code == 200

def test_not_auth_get_salary():
    """
        Получение информации о зарплате неавторизованным работником
    """
    response = client.get("/api/salary")
    assert response.status_code == 401

def test_auth_create_token():
    """
        Создание токена для авторизованного работника
    """
    response = client.post("/api/token", data={"username":var.username,"password":var.password})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_auth_wrong_create_token():
    """
        Создание токена для работника с некорректным логином
    """
    response = client.post("/api/token", data={"username":"wrong","password":var.password})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_password_wrong_create_token():
    """
        Создание токена для работника с некорректным password
    """
    response = client.post("/api/token", data={"username":"wrong","password":var.password})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
def test_not_auth_create_token():
    """
       Создание токена для неавторизованного работника
    """
    response = client.post("/api/token",)
    assert response.status_code == 422


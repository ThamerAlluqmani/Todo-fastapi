from fastapi.testclient import TestClient
import pytest
from app.api.main import app
from app.api.routes.auth.models import User
from app.api.utils_api.dependencies import get_db_session


@pytest.fixture
def client():
    return TestClient(app)


class TestAuth:
    def test_register_new_user(self, client):
        user_data = {
            "email": "thetest99@test.com",
            "password": "password",
            "phone": "966500000000",
            "name": "test",
        }
        # Act
        response = client.post("auth/signup", json=user_data)
        # Assert
        assert response.status_code == 201
        assert response.json() == {
            "email": "thetest99@test.com",
            "name": "test",
            "phone": "966500000000",
        }

    def test_login(self, client):
        user_data = {"email": "thetest99@test.com", "password": "password"}
        # Act
        response = client.post("auth/login", json=user_data)
        # get access token
        access_token = response.json()["access_token"]
        # Assert
        assert response.status_code == 200
        assert access_token is not None
        # make sure the token is valid
        response = client.get(
            "auth", headers={"Authorization": f"Bearer {access_token}"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "email": "thetest99@test.com",
            "name": "test",
            "phone": "966500000000",
        }
        # delete user using session
        session = next(get_db_session())
        session.query(User).filter(User.email == "thetest99@test.com").delete()
        session.commit()
        session.close()

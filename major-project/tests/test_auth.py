import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.database.connection import Base
from backend.main import app
from backend.api.auth import get_db


TEST_DATABASE_URL = "sqlite://"


engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


def test_register_user_successfully():
    response = client.post(
        "/api/auth/register",
        json={
            "username": "test_student",
            "password": "Test@12345"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User registered successfully"
    assert data["username"] == "test_student"


def test_login_successfully():
    client.post(
        "/api/auth/register",
        json={
            "username": "test_student",
            "password": "Test@12345"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "username": "test_student",
            "password": "Test@12345"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_with_wrong_password_is_rejected():
    client.post(
        "/api/auth/register",
        json={
            "username": "test_student",
            "password": "Test@12345"
        }
    )

    response = client.post(
        "/api/auth/login",
        json={
            "username": "test_student",
            "password": "WrongPassword"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


def test_duplicate_username_is_rejected():
    user = {
        "username": "duplicate_user",
        "password": "Test@12345"
    }

    first_response = client.post(
        "/api/auth/register",
        json=user
    )

    second_response = client.post(
        "/api/auth/register",
        json=user
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Username already exists"


def test_protected_endpoint_rejects_invalid_token():
    response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": "Bearer invalid-token"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or expired token"
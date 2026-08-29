from fastapi.testclient import TestClient

from backend.main import app
from backend.services.jwt import create_access_token


client = TestClient(app)


def test_student_is_forbidden_from_admin_endpoint():
    student_token = create_access_token(
        user_id=100,
        role="student"
    )

    response = client.get(
        "/api/auth/admin",
        headers={
            "Authorization": f"Bearer {student_token}"
        }
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Insufficient permissions"


def test_admin_can_access_admin_endpoint():
    admin_token = create_access_token(
        user_id=1,
        role="admin"
    )

    response = client.get(
        "/api/auth/admin",
        headers={
            "Authorization": f"Bearer {admin_token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Welcome, admin"
    assert data["user_id"] == "1"
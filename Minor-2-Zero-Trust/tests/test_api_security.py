import requests

BASE_URL = "http://localhost:8000"


def test_public_endpoint():
    response = requests.get(f"{BASE_URL}/api/public")
    assert response.status_code == 200


def test_employee_requires_authentication():
    response = requests.get(f"{BASE_URL}/api/employee")
    assert response.status_code == 401


def test_admin_requires_authentication():
    response = requests.get(f"{BASE_URL}/api/admin")
    assert response.status_code == 401


def test_employee_rejects_invalid_token():
    response = requests.get(
        f"{BASE_URL}/api/employee",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert response.status_code == 401


def test_admin_rejects_invalid_token():
    response = requests.get(
        f"{BASE_URL}/api/admin",
        headers={"Authorization": "Bearer invalid-token"},
    )
    assert response.status_code == 401
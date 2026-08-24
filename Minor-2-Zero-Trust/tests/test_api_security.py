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

def test_content_type_options_header():
    response = requests.get(f"{BASE_URL}/")
    assert response.headers.get("X-Content-Type-Options") == "nosniff"


def test_frame_options_header():
    response = requests.get(f"{BASE_URL}/")
    assert response.headers.get("X-Frame-Options") == "DENY"


def test_referrer_policy_header():
    response = requests.get(f"{BASE_URL}/")
    assert response.headers.get("Referrer-Policy") == "no-referrer"    
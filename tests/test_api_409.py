import requests

from env.env import API_URL



def test_registration_duplicate_email(generate_fake_data_with_confirm_password):
    requests.post(API_URL, json=generate_fake_data_with_confirm_password)
    response = requests.post(API_URL, json=generate_fake_data_with_confirm_password)
    assert response.status_code == 409, "Registration should fail with duplicate email"
    assert "An account already exists with the same email address" in response.text, "Error message should indicate email already exists"
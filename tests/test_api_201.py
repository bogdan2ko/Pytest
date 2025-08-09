import requests
from faker import Faker
from env.env import API_URL

fake = Faker()



def test_registration_api_success_simple(generate_fake_data):
    response = requests.post(API_URL, json=generate_fake_data)
    assert response.status_code == 201, "Registration should be successful with generated data"
    

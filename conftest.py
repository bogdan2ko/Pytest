import pytest
from faker import Faker

fake = Faker()

@pytest.fixture()
def generate_fake_data():
    """Fixture to generate fake data for tests."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": "securepassword"
    }


@pytest.fixture()
def generate_fake_data_with_confirm_password():
    """Fixture to generate fake data with confirm password for tests."""
    return {
        "name": "bog222",
        "email": "bogdanpog@gmail.com",
        "password": "Skyrimko234"
        # "confirm_password": "securepassword"
    }
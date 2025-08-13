from playwright.sync_api import Page
from faker import Faker

from pages.registration_page import RegistrationPage

fake=Faker()

def test_ui_registration_with_empty_fields(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form("", "", "")  # Empty values for negative test
    registration_page.submit()
    assert not registration_page.is_registration_successful() , "Registration should not be successful with empty fields"
    assert registration_page.has_empty_fields_error() is True , "Error message for empty fields should be displayed"

def test_ui_positive_registration(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(fake.user_name() , "ValidPassword123!", "ValidPassword123!")  # Valid data
    registration_page.submit()
    assert registration_page.is_registration_successful(), "Registration should be successful with valid data"
    assert not registration_page.has_empty_fields_error(), "Error message for empty fields should not be displayed"

def test_ui_registration_with_short_username(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form("ab", "ValidPassword123!", "ValidPassword123!")
    registration_page.submit()
    assert registration_page.has_short_username_error(), "Error message for short username should be displayed"

def test_ui_registration_with_uncorrect_passwords(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.fill_form(fake.user_name(), "short", "different")
    registration_page.submit()
    assert registration_page.has_uncorrect_passwords_error(), "Error message for mismatched passwords should be displayed"

def test_ui_registration_with_overly_long_username(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    overly_long_username = "a" * 256  # Assuming max length is 255
    registration_page.fill_form(overly_long_username, "ValidPassword123!", "ValidPassword123!")
    registration_page.submit()
    assert registration_page.has_invalid_username(), \
        "Error message for overly long username should be displayed"


def test_ui_registration_with_invalid_username(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    invalid_username = "Invalid@Username!"
    registration_page.fill_form(invalid_username, "ValidPassword123!", "ValidPassword123!")
    registration_page.submit()
    assert registration_page.has_invalid_username(), \
        "Error message for invalid username should be displayed"
    
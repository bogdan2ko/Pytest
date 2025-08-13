from playwright.sync_api import Page
from faker import Faker

from pages.login_page import LoginPage
fake=Faker()

def test_ui_login_successful(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_form("practice", "SuperSecretPassword!")
    login_page.submit()
    assert login_page.is_login_successful(), "Login should be successful with valid credentials"
    assert not login_page.has_already_logged_in_error(), "Error message for already logged in user should not be displayed"

def test_already_logged_in_redirect(page: Page):
    login_page = LoginPage(page)
    login_page.open()  # открываем /login
    login_page.fill_form("practice", "SuperSecretPassword!")
    login_page.submit()
    assert login_page.is_login_successful()  # убедились, что залогинились

    login_page.open()  # пытаемся открыть /login повторно

    # Проверяем, что нас редиректит на /secure
    assert "/secure" in page.url

    # И проверяем сообщение "You're logged in. Please log out before logging in as a different user"
    assert login_page.has_already_logged_in_error()



def test_ui_login_with_invalid_username(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    overly_long_username = "a" * 256  # Assuming the max length is 255 characters
    login_page.fill_form(overly_long_username, "wwwwwwwwwwwwwwwwwww")
    login_page.submit()
    
    assert not login_page.is_login_successful(), \
        "Login should not be successful with invalid username"
    assert login_page.has_username_invalid_error(), \
        "Error message for invalid username should be displayed"
    
def test_ui_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_form("practice", "wrongpassword")
    login_page.submit()

    assert not login_page.is_login_successful(), \
        "Login should not be successful with invalid password"
    assert login_page.has_password_invalid_error(), \
        "Error message for invalid password should be displayed"
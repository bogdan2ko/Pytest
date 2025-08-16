from playwright.sync_api import Page
from faker import Faker

from pages.Secure_Password_Checker import SecurePasswordCheckerPage
fake=Faker()

def test_secure_password_checker_long_enough(page: Page):
    checker_page = SecurePasswordCheckerPage(page)
    checker_page.open()
    checker_page.fill_password("Short1")
    assert checker_page.must_be_long_enough(), "Must be at least 8 characters long."

def test_secure_password_checker_uppercase(page: Page):
    checker_page = SecurePasswordCheckerPage(page)
    checker_page.open()
    checker_page.fill_password("lowercase1")
    assert checker_page.must_contain_uppercase(), "Must contain an uppercase letter."

def test_secure_password_checker_lowercase(page: Page):
    checker_page = SecurePasswordCheckerPage(page)
    checker_page.open()
    checker_page.fill_password("UPPERCASE1")
    assert checker_page.must_contain_lowercase(), "Must contain a lowercase letter."

def test_secure_password_checker_number(page: Page):
    checker_page = SecurePasswordCheckerPage(page)
    checker_page.open()
    checker_page.fill_password("NoNumberOrSpecialChar")
    assert checker_page.must_contain_number(), "Must contain an uppercase letter."
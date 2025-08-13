
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://practice.expandtesting.com/login")

    def fill_form(self, username: str, password: str):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)

    def submit(self):
        self.page.get_by_role("button", name="Login").click()

    def is_login_successful(self):
        try:
            return "/secure" in self.page.url and \
                self.page.wait_for_selector("text=You logged into a secure area!").is_visible()
        except:
            return False
            
    def has_already_logged_in_error(self):
        try:
            # Ищем по части сообщения, чтобы избежать проблем с точным совпадением
            return self.page.locator("text=Please log out before logging in").is_visible(timeout=3000)
        except:
            return False


    def has_username_invalid_error(self):
        try:
            return self.page.locator("text=Your username is invalid!").is_visible(timeout=3000)
        except:
            return False
        
    
    def has_username_invalid_error(self):
        try:
            return "/login" in self.page.url and \
                self.page.wait_for_selector("text=Your username is invalid!").is_visible()
        except:
            return False
    
    def has_password_invalid_error(self):
        try:   
            return "/login" in self.page.url and \
                self.page.wait_for_selector("text=Your password is invalid!").is_visible()
        except:
            return False
            
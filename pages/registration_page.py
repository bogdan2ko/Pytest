from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://practice.expandtesting.com/register")

    def fill_form(self, username: str, password: str, confirm_password: str):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password", exact=True).fill(password)
        self.page.get_by_role("textbox", name="Confirm Password").fill(confirm_password)

    def submit(self):
        self.page.get_by_role("button", name="Register").click()

    def is_registration_successful(self):
        try:
            return "/login" in self.page.url and \
                self.page.wait_for_selector("text=Successfully registered, you can log in now.").is_visible()
        except:
            return False
        
    def has_empty_fields_error(self):
        # Проверяем наличие ошибки "All fields are required"
        try:
            self.page.wait_for_selector("text=All fields are required", timeout=3000)
            return True
        except:
            return False

    def has_duplicate_email_error(self):
        try:
            self.page.wait_for_selector("text=Email already exists", timeout=3000)
            return True
        except:
            return False

    def has_short_username_error(self):
        try:
            self.page.wait_for_selector("text=Username must be at least 3 characters long.", timeout=3000)
            return True
        except:
            return False
        
    def has_uncorrect_passwords_error(self):
        try:
            self.page.wait_for_selector("text=Passwords do not match.", timeout=3000)
            return True 
        except:
            return False
        

    def has_invalid_username(self):
        try:
            return "/register" in self.page.url and \
                self.page.wait_for_selector("text=Invalid username. Usernames can only contain lowercase letters, numbers, and single hyphens, must be between 3 and 39 characters, and cannot start or end with a hyphen.").is_visible()
        except:
            return False
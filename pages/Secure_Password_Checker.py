from playwright.sync_api import Page

class SecurePasswordCheckerPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://practice.expandtesting.com/secure-password-checker")


    def fill_password(self, password: str):
        textbox = self.page.get_by_role("textbox")
        textbox.click()
        textbox.type(password, delay=100)  # печатаем с задержкой, чтобы не исчезало

    
    def must_be_long_enough(self):
        try:
            return self.page.locator("text=Must be at least 8 characters long.").is_visible(timeout=3000)
        except:
            return False
    
    def must_contain_uppercase(self):
        try:
            return self.page.locator("text=Must contain an uppercase letter.").is_visible(timeout=3000)
        except:
            return False
        
    def must_contain_lowercase(self):
        try:
            return self.page.locator("text=Must contain a lowercase letter.").is_visible(timeout=3000)
        except:
            return False
        
    def must_contain_number(self):
        try:
            return self.page.locator("text=Must contain a number or special character.").is_visible(timeout=3000)
        except:
            return False

from playwright.sync_api import expect
from utils.base_page import BasePage


class LoginPage(BasePage):
    # Initialize LoginPage by calling BasePage constructor
    def __init__(self, page):
        super().__init__(page)

    # Method for login functionality with valid credential
    def login(self, username, password):
        # Wait for Email field before filling
        self.page.wait_for_selector('input[placeholder="Enter your mail"]')
        self.page.fill('input[placeholder="Enter your mail"]', username)
        self.page.locator('input[placeholder="Enter your mail"]').fill(username)

        # Wait for Password field before filling
        self.page.wait_for_selector('input[placeholder="Enter your password "]')
        self.page.fill('input[placeholder="Enter your password "]', password)
        self.page.locator('input[placeholder="Enter your password "]').fill(password)

        # Wait for Sign In button before clicking
        self.page.wait_for_selector('button:has-text("Sign in")')
        self.page.click('button:has-text("Sign in")')

    # Method to validate visibility of essential input fields
    def validate_inputs(self):
        assert self.page.get_by_role("textbox", name="Email").is_visible()
        assert self.page.get_by_role("textbox", name="Password").is_visible()

    # Method to close the popup
    def close_popup_if_present(self):
        try:
            self.page.get_by_role("button", name="Close popup").click()
        except:
            pass  # Handle cases where popup isn’t present

    #  Method for login functionality with invalid credential
    def login_with_invalid_data(self, username: str, password: str):
        self.page.goto("https://v2.zenclass.in/login")  # Navigate to login page

        self.page.fill('input[placeholder="Enter your mail"]', username)
        self.page.fill('input[placeholder="Enter your password "]', password)
        self.page.click("button[type='submit']") # Attempt to login

        self.page.wait_for_timeout(1000) # Small wait to allow error message to appear




from playwright.sync_api import Page, expect
import time

# BasePage class created
class BasePage:
    def __init__(self, page: Page):
        self.page = page  # Store the Playwright Page object for use in other methods


    def wait_for_element(self, locator: str, timeout: int = 5000):
        # Wait until the element matching the locator appears on the page

        self.page.wait_for_selector(locator, timeout=timeout)
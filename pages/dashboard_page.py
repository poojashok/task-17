from utils.base_page import BasePage

class DashboardPage:
    def __init__(self, page):
        self.page = page # Store the Playwright Page object for dashboard interactions


    def logout(self):
        # Click on the profile icon to open the dropdown menu
        self.page.locator("#profile-click-icon").click()

        # Click the "Log out" option in the dropdown
        self.page.get_by_text("Log out").click()



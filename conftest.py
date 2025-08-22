import pytest
from playwright.sync_api import sync_playwright

# Fixture to create and manage browser context for each test

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
    # Launch Playwright and a Chromium browser instance

        browser = p.chromium.launch(headless=False)
        # Headless=False enables browser UI

        context = browser.new_context()
        # Create isolated browser context

        yield context    # Yield context to the test
        context.close()  # Close the context
        browser.close()  # Close the browser

# Fixture to create and manage a new page
@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page() # Open a new tab
    yield page  # Yield page for test
    page.close()  # Close the tab
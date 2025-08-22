import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize(
    "username, password",
    [
        # Positive test case with valid credentials
        ("poojanand0928@gmail.com", "dITVI@1209"),
    ]
)
def test_login(page, username, password):

    # Initialize Page Objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Step 1: Navigate to the login page
    page.goto("https://v2.zenclass.in/login")
    page.wait_for_load_state("networkidle")  # Wait until page and network calls are idle
    print("[INFO] Navigated to ZenClass login page.")

    # Step 2: Perform login
    login_page.login(username, password)
    login_page.close_popup_if_present()  # Handle any post-login popup
    print(f"[INFO] Attempted login with {username}. Current URL: {page.url}")

    # Step 3: Validate login success
    assert page.url == "https://v2.zenclass.in/dashboard", \
        f"[ERROR] Login failed. Expected dashboard, got {page.url}"
    print("[PASS] Login successful. User redirected to dashboard.")

    # Step 4: Capture screenshot after login
    page.screenshot(path="valid_login.png")

    # Step 5: Perform logout
    dashboard_page.logout()
    print(f"[INFO] Logout performed. Current URL: {page.url}")

    # Step 6: Validate logout success
    page.wait_for_url("https://v2.zenclass.in/login", timeout=10000)
    assert page.url == "https://v2.zenclass.in/login", \
        f"[ERROR] Logout failed. Expected login page, got {page.url}"
    print("[PASS] Logout successful. User redirected to login page.")

    # Step 7: Capture screenshot after logout
    page.screenshot(path="after_logout.png")


def test_invalid_login(page):

    # Initialize Page Object
    login_page = LoginPage(page)

    # Step 1 & 2: Attempt login with invalid credentials
    page.goto("https://v2.zenclass.in/login")
    login_page.login_with_invalid_data("wrong@example.com", "Wrong111")
    print("[INFO] Attempted login with invalid credentials.")

    # Step 3: Capture screenshot after invalid login attempt
    page.screenshot(path="invalid_login.png")

    # Step 4: Validate redirection - should remain on login page
    assert page.url == "https://v2.zenclass.in/login", \
        f"[ERROR] Invalid login redirected unexpectedly. Current URL: {page.url}"

    # Step 5: Validate error message visibility
    assert page.is_visible("text=Invalid email!"), \
        "[ERROR] Expected 'Invalid email!' error message not displayed."
    print("[PASS] Invalid login detected correctly. Error message displayed.")

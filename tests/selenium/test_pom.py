from pages.login_page import LoginPage
import pytest
import time

@pytest.mark.login
@pytest.mark.e2e
def test_login_functionality(chrome_browser):

    url = "https://practicetestautomation.com/practice-test-login/"
    login_page = LoginPage(chrome_browser)

    login_page.open_page(url)

    login_page.enter_username("student")
    login_page.enter_password("Password123")

    login_page.click_login()

    assert login_page.verify_success_login()

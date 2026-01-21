import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.basic_playwright
def test_has_title(page: Page):

    page.goto("https://playwright.dev/")

    expect(page).to_have_title(re.compile("Playwright"))

@pytest.mark.login
def test_login(page: Page):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.get_by_label("username").fill("student")
    page.get_by_label("password").fill("Password123")


    page.get_by_role("button", name="submit").click()

    expect(page.get_by_text(re.compile("Congratulations"))).to_be_visible()

    expect(page.get_by_text(re.compile("Log out"))).to_be_visible()



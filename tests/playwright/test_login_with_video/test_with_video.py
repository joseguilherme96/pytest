from pytest import mark
import re
from playwright.sync_api import Page, expect, Browser

@mark.login
@mark.e2e
def test_login_with_video(page: Page,browser: Browser):

    context = browser.new_context(record_video_dir="tests/playwright/test_login_with_video/")

    page = context.new_page()

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.get_by_label("username").fill("student")
    page.get_by_label("password").fill("Password123")


    page.get_by_role("button", name="submit").click()

    expect(page.get_by_text(re.compile("Congratulations"))).to_be_visible()

    expect(page.get_by_text(re.compile("Log out"))).to_be_visible()

    context.close()
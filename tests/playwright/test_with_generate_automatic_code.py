import re
from playwright.sync_api import Playwright, sync_playwright, expect
from pytest import mark

@mark.e2e
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    expect(page.locator("h2")).to_contain_text("Test login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("button", name="Submit").click()
    page.locator("#error").click()
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_text("Password123").first.click()
    page.get_by_role("textbox", name="Password").click(modifiers=["Shift"])
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("article")).to_contain_text("Log out")
    page.get_by_role("link", name="Log out").click()

    # ---------------------
    context.close()
    browser.close()

if __name__ == '__main__':

    with sync_playwright() as playwright:
        test_run(playwright)

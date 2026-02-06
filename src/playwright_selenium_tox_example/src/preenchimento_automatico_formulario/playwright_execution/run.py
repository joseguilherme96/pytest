from playwright.sync_api import sync_playwright


def navegator(page) -> None:

    page.goto("https://practicetestautomation.com/contact/")
    page.locator("#wpforms-161-field_0").fill("José")
    page.locator("#wpforms-161-field_0-last").fill("Guilherme")


if __name__ == "__main__":
    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        navegator(page)

        page.wait_for_event("close")

        context.close()
        context.browser.close()

    except Exception as e:
        print(f"Ocorreu um erro {e}")

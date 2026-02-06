from preenchimento_automatico_formulario.playwright_execution.run import navegator
from playwright.sync_api import sync_playwright


def test_navegator():

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(
                record_video_dir="tests/playwright/",
                record_video_size={"width": 1920, "height": 1080},
                viewport={"width": 1920, "height": 1080},
            )
            page = context.new_page()

            navegator(page)

            page.wait_for_event("close")

            context.close()
            playwright.stop()

    except Exception as e:
        print(f"Ocorreu um erro {e}")

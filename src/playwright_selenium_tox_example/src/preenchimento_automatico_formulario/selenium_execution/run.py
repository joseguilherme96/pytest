from preenchimento_automatico_formulario.selenium_execution.page.contact_page import ContactPage
from preenchimento_automatico_formulario.selenium_execution.utils.functions import wait_until_browser_closed,configure_webdriver
from pathlib import Path
import os
from dotenv import load_dotenv

def navegator(chrome_browser):

    page = ContactPage(chrome_browser)
    page.open_page("https://practicetestautomation.com/contact/")
    page.enter_name("José")
    page.enter_last_name("Guilherme")


if __name__ == "__main__":

    load_dotenv()
    
    browser_path = os.getenv("BROWSER_PATH")
    driver_path = os.getenv("DRIVER_PATH")

    driver = configure_webdriver(str(browser_path), str(driver_path))
    driver.implicitly_wait(20)

    navegator(driver)

    wait_until_browser_closed(driver)

    driver.quit()
    
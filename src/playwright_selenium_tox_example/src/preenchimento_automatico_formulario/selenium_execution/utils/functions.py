from selenium.common.exceptions import WebDriverException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

def wait_until_browser_closed(driver, poll=0.5):
    while True:
        try:
            driver.title
            time.sleep(poll)
        except WebDriverException:
            break

def configure_webdriver(browser_path, driver_path):
    chrome_options = Options()
    chrome_options.binary_location = browser_path

    service = ChromeService(executable_path=driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver
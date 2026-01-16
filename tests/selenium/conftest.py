from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def chrome_browser():

    driver = webdriver.Chrome()

    driver.implicitly_wait(20)

    yield driver

    driver.quit()
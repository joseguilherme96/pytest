from pytest import fixture
from preenchimento_automatico_formulario.selenium_execution.utils.functions import wait_until_browser_closed,configure_webdriver
import os
from dotenv import load_dotenv

def pytest_addoption(parser):

    load_dotenv()

    browser_path = os.getenv("BROWSER_PATH")
    driver_path = os.getenv("DRIVER_PATH")

    parser.addoption(
        "--browser-path",
        action="store",
        default=browser_path,
        type=str,
        help="Type in browser name e.g. chrome"
    )

    parser.addoption(
        "--driver-path",
        action="store",
        default=driver_path,
        type=str,
        help="Type in url name"
    )

@fixture
def browser_path(request):
    return request.config.getoption("--browser-path")

@fixture
def driver_path(request):
    return request.config.getoption("--driver-path")

@fixture
def chrome_browser(browser_path,driver_path):

    driver = configure_webdriver(browser_path, driver_path)
    driver.implicitly_wait(20)

    yield driver

    wait_until_browser_closed(driver)

    driver.quit()
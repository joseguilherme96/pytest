import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pytest import mark

@mark.e2e
def test_title(chrome_browser):  
    """  
    Test the title of the Python.org website  
    """  
    chrome_browser.get("https://www.python.org")  
    assert chrome_browser.title == "Welcome to Python.org"
    time.sleep(10)

@mark.e2e
def test_search(chrome_browser):

    url = "https://duckduckgo.com/"
    search_term = "Pytest With Eric"

    chrome_browser.get(url)

    search_box = chrome_browser.find_element(By.ID,value="searchbox_input")

    search_box.send_keys(search_term + Keys.RETURN)

    assert search_term in chrome_browser.title
    time.sleep(10)

@mark.e2e
def test_login_functionnality(chrome_browser):

    url = "https://practicetestautomation.com/practice-test-login/"

    chrome_browser.get(url)

    chrome_browser.find_element(By.ID,"username").send_keys("student")
    chrome_browser.find_element(By.ID,"password").send_keys("Password123")

    chrome_browser.find_element(By.ID,"submit").click()

    try:

        logout_button = chrome_browser.find_element(
            By.CLASS_NAME, "wp-block-button__link"
        )

        assert logout_button.is_displayed(), "Logout button is not displayed."

    except NoSuchElementException:

        assert False, "Logout button does not exist."

    try:

        logout_button = chrome_browser.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed(), "Logout button is not displayed."

    except NoSuchElementException:
        assert False, "Logout button does not exist."

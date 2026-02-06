from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactPage:
    def __init__(self, driver):

        self.driver = driver

    def open_page(self, url):

        self.driver.get(url)

    def enter_username(self, username):

        self.driver.find_element(By.ID, "login").send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(By.ID, "senha").send_keys(password)

    def enter_name(self, name):

        self.driver.find_element(By.ID, "wpforms-161-field_0").send_keys(name)

    def enter_last_name(self, last_name):

        self.driver.find_element(By.ID, "wpforms-161-field_0-last").send_keys(last_name)

    def wait_iframe(self):

        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
        )

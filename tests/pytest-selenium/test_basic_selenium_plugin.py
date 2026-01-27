from selenium.webdriver.common.by import By
from pytest import mark

@mark.e2e
def test_pytest_selenium_plugin_example(selenium):

    selenium.get("https://pytest-with-eric.com")

    selenium.implicitly_wait(20)
    assert selenium.title == "Welcome to Pytest with Eric! | Pytest with Eric"

    meta_description = selenium.find_element(By.XPATH, "//meta[@name='description']")

    content_value = meta_description.get_attribute("content")

    expected_content = "Learn to write simple but effective tests with Pytest.  From basics to advanced topics with simple, but detailed explanations and example code. Explore the topics below or on the sidebar to get starte"

    assert content_value == expected_content
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


# install pytest-html for generating html report

driver= None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("setup ")
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print("tear down")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title=="Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url=="https://www.google.com/"
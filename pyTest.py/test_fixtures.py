from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# install pytest-html for generating html report

driver= None

def setup_module(module):
    global driver
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_module():
    driver.quit()

def test_google_title():
    assert driver.title=="Google"

def test_google_url():
    assert driver.current_url=="https://www.google.com/"
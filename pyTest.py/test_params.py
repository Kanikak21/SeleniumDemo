import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubspot(BaseTest):

    @pytest.mark.parametrize(

        "username, password",
        [
            ("admin@gmail.com","admin@123"),
            ("admin@gmail.com","admin@123"),
        ]
    )

    def test_login(self,username,password):
        self.driver.get("https://www.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)   
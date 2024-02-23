import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def input_total():
    total = 100
    return total

# @pytest.fixture(params=['Chrome','Firefox'])
# def driver_access(request):
#     if request.param== 'Chrome':
#         driver=webdriver.Chrome()
#     if request.param== 'Firefox':
#         driver=webdriver.Firefox()

#     return driver


@pytest.fixture(params=['Chrome','Firefox'], scope='class')
def init_driver(request):
    if request.param== 'Chrome':
        driver=webdriver.Chrome()
    if request.param== 'Firefox':
        driver=webdriver.Firefox()
    request.cls.driver= driver 
    driver.implicitly_wait(20)
    yield
    driver.close()   

   



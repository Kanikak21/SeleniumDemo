import pytest
import time


# def test_divisible_by_6(input_total):
#     assert input_total % 6 ==0
   
# def test_divisible_by_5(input_total):
#     assert input_total % 5 ==0  

def test_openbrowser(driver_access,enter_text):
    driver_access.get('https://www.google.com')
    time.sleep(10)

    
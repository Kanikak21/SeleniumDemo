import pytest

# start with test or end with test 

def test_m1():

    a=1
    b=4
    assert a+1==b, "test failed"
    assert a==b, "a is not equal to b- test failed "

def test_m2():
    name= "Selenium"
    assert name.upper()== "SELENIUM"

def test_login():
    assert "admin"=="admin"
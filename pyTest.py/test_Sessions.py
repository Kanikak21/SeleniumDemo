import pytest

# start with test or end with test 

@pytest.mark.login
def test_m1():

    a=1
    b=4
    assert a+1==b, "test failed"
    assert a==b, "a is not equal to b- test failed "

def test_m2():
    name= "Selenium"
    assert name.upper()== "SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert False

def test_m5():
    assert 100==100    

@pytest.mark.login
def test_login_FB():
    assert "admin"=="123"
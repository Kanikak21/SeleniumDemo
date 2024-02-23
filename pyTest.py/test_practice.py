import pytest

@pytest.mark.login
def test_m3():
    assert True

def test_m4():
    assert False

def test_m5():
    assert 100==100 

@pytest.mark.login
def test_login_Insta():
    assert "admin"=="admin"
'''
1. Add @pytest.mark.xxx before each test cases
2. To run test cases depending on mark name:
    pytest Use_pytest_mark.py -m more -v
    or
    pytest Use_pytest_mark.py -m less -v
'''
import pytest

# Functions
def Add(a, b):
    return a + b

def Minus(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    return a / b

# Test cases (started with "test")
@pytest.mark.more
def test_add():
    assert Add(2, 3) == 5

@pytest.mark.more
def test_add_false():
    assert Add(2, 3) == 6

@pytest.mark.less
def test_minus():
    assert Minus(5, 3) == 2

@pytest.mark.more
def test_multiply():
    assert Multiply(2, 3) == 6

@pytest.mark.five
def test_divide():
    assert Divide(6, 3) == 2
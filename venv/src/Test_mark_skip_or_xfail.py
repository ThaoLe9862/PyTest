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
def test_add():
    assert Add(2, 3) == 5

@pytest.mark.xfail
def test_add_false():
    assert Add(2, 3) == 6

@pytest.mark.skip
def test_minus():
    assert Minus(5, 3) == 2

def test_multiply():
    assert Multiply(2, 3) == 6

def test_divide():
    assert Divide(6, 3) == 2
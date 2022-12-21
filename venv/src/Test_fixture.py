'''
If not use @pytest.fixture, we cannot use array_numbers as parameters.
To run test using command: pytest Test_fixture.py
'''
import pytest

@pytest.fixture
def array_numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]

def test_arr_index_0(array_numbers):
    assert array_numbers[0] == 10

def test_arr_index_1(array_numbers):
    assert array_numbers[1] == 20

def test_arr_index_2(array_numbers):
    assert array_numbers[2] == 25

def test_arr_index_3(array_numbers):
    assert array_numbers[3] == 25
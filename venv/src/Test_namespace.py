import pytest
global id
id = 0
@pytest.fixture
def data():
    return 0

def test(data):
    assert id == 0

def test_update(data):
    global id
    id = 200
    #pytest.my_global_variable = 200

def test_confirm(data):
    assert id == 200
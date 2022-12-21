import pytest
import requests
import json
'''
def main_url():
    return "https://regres.in"


def test_login_valid():
    url = "https://regres.in/api/login/"
    data = {"email": "eve.holt@regres.in", "password": "cityslicka"}
    response = requests.post(url, data = data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == 'QpwL5tke4Pnpja7X4'
'''

# Reference: https://web.postman.co/workspace/My-Workspace~7e5f01c7-94a1-4778-85b3-d85e2f0b4d8a/request/24910528-a858c80d-a703-4b8e-a3b8-07d737c3f316
def test_api():
    url = "https://postman-echo.com/post?set_start_day=August 19, 2022"
    response = requests.post(url)
    assert response.status_code == 200

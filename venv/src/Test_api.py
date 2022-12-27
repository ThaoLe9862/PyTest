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
def test_api():
    url = "https://postman-echo.com/post?set_start_day=August 19, 2022"
    response = requests.post(url)
    assert response.status_code == 200

# Reference: https://web.postman.co/workspace/My-Workspace~7e5f01c7-94a1-4778-85b3-d85e2f0b4d8a/run/create?collection=24910528-5f0a648c-8613-4fc0-83e5-aeab991b438d&type=manual-run
@pytest.fixture
def baseURL():
    url = "https://simple-books-api.glitch.me"
    return url

@pytest.fixture
def accessToken():
    return "49896332d65cc5ee6701ac2521b5a66406c9360f3d0c20a9cf5fddfa488be29a"

def test_check_API_work(baseURL):
    response = requests.get(baseURL)
    assert response.status_code == 200

def test_check_API_message(baseURL):
    expected = "Welcome to the Simple Books API."
    response = requests.get(baseURL)
    assert expected in response.text

def test_status(baseURL):
    response = requests.get(baseURL + "/status")
    assert response.status_code == 200

def test_get_list_books(baseURL):
    response = requests.get(baseURL + "/books")
    #assert "fiction" in response.text
    #assert "non-fiction" in response.text
    assert response.status_code == 200

def test_single_book(baseURL):
    # Get book with bookid = 1
    path_variables = {"bookid": 1}
    response = requests.get(baseURL + "/books/", params = path_variables)
    assert response.status_code == 200

def test_get_list_fiction_books(baseURL):
    query_params = {"type": "fiction"}
    response = requests.get(baseURL + "/books/", params = query_params)
    assert response.status_code == 200 and "fiction" in response.text

def test_get_list_non_fiction_books_and_limit_3(baseURL):
    # query non-fiction book and show maximun 3 records
    query_params = {"type": "non-fiction", "limit": 3}
    response = requests.get(baseURL + "/books/", params = query_params)
    assert response.status_code == 200 and "non-fiction" in response.text

#@pytest.mark.skip
def test_post_API_Authentication(baseURL, accessToken):
    input_body = {"clientName": "Valentino", "clientEmail": "valentino@example.com"}
    response = requests.post(baseURL + "/api-clients/", json = input_body)
    assert response.status_code == 409

def test_post_order_book(baseURL, accessToken):
    header = {"Authorization": "Bearer " + accessToken}
    jsonData = { "bookId": 1, "customerName": "David" }
    response = requests.post(baseURL + "/orders/", headers = header, json = jsonData)
    #response = requests.request("POST", baseURL + "/orders/", )
    assert  response.status_code == 201

#@pytest.mark.skip
def test_get_list_orders(baseURL, accessToken):
    header = {"Authorization": "Bearer " + accessToken}
    path_variables = {"bookid": 1}
    response = requests.get(baseURL + "/orders/", params=path_variables, headers=header)
    assert response.status_code == 200

#@pytest.mark.skip
def test_update_list_order(baseURL, accessToken):
    header = {"Authorization": "Bearer " + accessToken}
    id = "VLBZtDCeR7q-9GAyGhX09" # path_variables = {"id": "VLBZtDCeR7q-9GAyGhX09"}
    input_body = {"customerName": "Sumi Bowling"}
    response = requests.patch(baseURL + "/orders/" + id, headers=header, json=input_body)
    assert response.status_code == 204

#@pytest.mark.skip
def test_delete_order(baseURL, accessToken):
    header = {"Authorization": "Bearer " + accessToken}
    #path_variables = {"id": "8YtkszGI5JykOEjBa1uAu"}
    id = "VLBZtDCeR7q-9GAyGhX09"
    #response = requests.delete(baseURL + "/orders/", headers=header, params=path_variables, json=input_body)
    response = requests.delete(baseURL + "/orders/" + id, headers=header)
    assert response.status_code == 204

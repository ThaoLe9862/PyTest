# To run this file using command: python3 Test_api_basic.py
import requests
import json
'''
# Test 1: run OK
payload = {
    "name": "morpheus",
    "job": "leader"
}
resp = requests.post("https://regres.in/api/users", data = payload)
print(resp)
'''
baseURL = "https://simple-books-api.glitch.me"
accessToken ="49896332d65cc5ee6701ac2521b5a66406c9360f3d0c20a9cf5fddfa488be29a"
'''
# Test 2: run OK
header = {'Authorization': 'Bearer ' + accessToken}
path_variables = {"bookid": 1}
response = requests.get(baseURL + "/orders/", json=path_variables, headers=header)
print(response.text)
print(response)


# Test 3 : run OK
input_body = { 'clientName': 'Valentino', 'clientEmail': 'valentino@example.com' }
response = requests.post(baseURL + "/api-clients/", json = input_body)
print(response.json())
print(response)
'''

'''
# Test 4: run OK
header = {"Authorization": "Bearer " + accessToken}
path_variables = {"bookid": 1}
response = requests.get(baseURL + "/orders/", params=path_variables, headers=header)
print(response.json())
print((response))
'''
'''
# Test 5: run OK
header = {"Authorization": "Bearer " + accessToken}
path_variables = {"id": "VLBZtDCeR7q-9GAyGhX09"}
input_body = {"customerName": "Sumi"}
id = "VLBZtDCeR7q-9GAyGhX09"
response = requests.patch(baseURL + "/orders/" + id, headers=header, json=input_body)
#response = requests.patch(baseURL + "/orders/:id", headers=header, params=path_variables)
print(response.text)
print(response)
'''

# Test 6:
# Create new order
header = {"Authorization": "Bearer " + accessToken}
jsonData = { "bookId": 1, "customerName": "David" }
response = requests.post(baseURL + "/orders/", headers = header, json = jsonData)
print("response.text: " + response.text)
#print("response : " + response)
ret = json.loads(response.text)
print(ret["orderId"])

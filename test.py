import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/2")
print(response.json())

input()

response = requests.patch(BASE + "video/2", {"views": 98})
print(response.json())
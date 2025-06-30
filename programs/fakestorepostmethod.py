
import requests
# POST Create a Product
def create_product():
    payload = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }
    response = requests.post("https://fakestoreapi.com/products", json=payload)
    print("POST Create a Product:")
    print(response.json())

create_product()

#####################################################################
import requests
import os

token = "fdsfasfafdxzfdasasfasfddafs" # Set your GitHub token in environment variable
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

data = {
    "name": "my-new-repo",
    "description": "Created via REST API",
    "private": False
}

response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
print(response.json())

response = requests.post("https://api.github.com/user/repos",  json=data,auth=('giridhar276','yourtoken'))
print(response.json())
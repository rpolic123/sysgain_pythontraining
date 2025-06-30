


import requests
import json
def get_all_products():
    url= "https://fakestoreapi.com/"
    endpoint = "products"
    response = requests.get(url + endpoint)
    print("GET All Products:")
    data = response.json()
    for item in data:
        print("ID         :",item['id'])
        print("Item       :",item['title'])
        print("Description:",item['description'])
        print("price      :",item['price'])
        print("-------")
get_all_products()
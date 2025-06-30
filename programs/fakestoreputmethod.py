

import requests
def update_product(product_id):
    data = {
        "title": "updated product",
        "price": 15.0,
        "description": "updated description",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }
    response = requests.put(f"https://fakestoreapi.com/products/{product_id}", json=data)
    print("PUT Update a Product:")
    print(response.json())


update_product(10)
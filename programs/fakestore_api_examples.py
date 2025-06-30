import requests

# E-commerce API: Fake Store API
# Base URL: https://fakestoreapi.com

# GET All Products
def get_all_products():
    response = requests.get("https://fakestoreapi.com/products")
    print("GET All Products:")
    print(response.json())

# POST Create a Product
def create_product():
    data = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }
    response = requests.post("https://fakestoreapi.com/products", json=data)
    print("POST Create a Product:")
    print(response.json())

# PUT Update a Product
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

# DELETE a Product
def delete_product(product_id):
    response = requests.delete(f"https://fakestoreapi.com/products/{product_id}")
    print("DELETE a Product:")
    print(response.status_code)

if __name__ == "__main__":
    get_all_products()
    create_product()
    update_product(100)  # Replace with a valid product ID
    get_all_products()
    delete_product(1)  # Replace with a valid product ID

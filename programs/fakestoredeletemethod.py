

import requests
# DELETE a Product
def delete_product(product_id):
    response = requests.delete(f"https://fakestoreapi.com/products/{product_id}")
    print("DELETE a Product:")
    print(response.status_code)


delete_product(1)
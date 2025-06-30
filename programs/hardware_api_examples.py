import requests

# Hardware API: Mock API
# Base URL: https://mockapi.io/projects/64b8f1701e6aa7165ee9c669

# GET List of CPUs
def get_list_of_cpus():
    response = requests.get("https://mockapi.io/projects/64b8f1701e6aa7165ee9c669/cpus")
    print("GET List of CPUs:")
    print(response.json())

# GET Specific CPU Details
def get_cpu_details(cpu_id):
    response = requests.get(f"https://mockapi.io/projects/64b8f1701e6aa7165ee9c669/cpus/{cpu_id}")
    print(f"GET CPU Details for {cpu_id}:")
    print(response.json())

# POST Create a new CPU
def create_cpu():
    data = {
        "name": "Intel Core i9-11900K",
        "cores": 8,
        "threads": 16,
        "base_clock": "3.5GHz",
        "boost_clock": "5.3GHz"
    }
    response = requests.post("https://mockapi.io/projects/64b8f1701e6aa7165ee9c669/cpus", json=data)
    print("POST Create a new CPU:")
    print(response.json())

# PUT Update an existing CPU
def update_cpu(cpu_id):
    data = {
        "name": "Intel Core i9-11900K",
        "cores": 8,
        "threads": 16,
        "base_clock": "3.6GHz",  # Updated value
        "boost_clock": "5.3GHz"
    }
    response = requests.put(f"https://mockapi.io/projects/64b8f1701e6aa7165ee9c669/cpus/{cpu_id}", json=data)
    print(f"PUT Update CPU with id {cpu_id}:")
    print(response.json())

# DELETE an existing CPU
def delete_cpu(cpu_id):
    response = requests.delete(f"https://mockapi.io/projects/64b8f1701e6aa7165ee9c669/cpus/{cpu_id}")
    print(f"DELETE CPU with id {cpu_id}:")
    print(response.status_code)

if __name__ == "__main__":
    get_list_of_cpus()
    create_cpu()
    update_cpu("existing-cpu-id")  # Replace with an existing CPU ID
    delete_cpu("existing-cpu-id")  # Replace with an existing CPU ID

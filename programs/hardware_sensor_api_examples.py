
import requests

# Weather API: OpenWeatherMap API
# Base URL: https://api.openweathermap.org/data/2.5

# GET Current Weather Data
def get_current_weather(api_key, city):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    print("GET Current Weather Data:")
    print(response.json())

# GET 5-Day Weather Forecast
def get_weather_forecast(api_key, city):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")
    print("GET 5-Day Weather Forecast:")
    print(response.json())

# Mock example for POST Create a new sensor data
def create_sensor_data():
    data = {
        "sensor_id": "12345",
        "temperature": 22.5,
        "humidity": 60,
        "pressure": 1012
    }
    # For demonstration purposes, we're using a mock URL
    response = requests.post("https://example.com/api/sensors", json=data)
    print("POST Create new Sensor Data:")
    print(response.json())

# Mock example for PUT Update existing sensor data
def update_sensor_data(sensor_id):
    data = {
        "temperature": 23.0,  # Updated value
        "humidity": 58,
        "pressure": 1011
    }
    # For demonstration purposes, we're using a mock URL
    response = requests.put(f"https://example.com/api/sensors/{sensor_id}", json=data)
    print(f"PUT Update Sensor Data with id {sensor_id}:")
    print(response.json())

# Mock example for DELETE existing sensor data
def delete_sensor_data(sensor_id):
    # For demonstration purposes, we're using a mock URL
    response = requests.delete(f"https://example.com/api/sensors/{sensor_id}")
    print(f"DELETE Sensor Data with id {sensor_id}:")
    print(response.status_code)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = "London"
    get_current_weather(api_key, city)
    get_weather_forecast(api_key, city)
    create_sensor_data()  # Mock example
    update_sensor_data("12345")  # Mock example
    delete_sensor_data("12345")  # Mock example

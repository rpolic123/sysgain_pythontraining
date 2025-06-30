
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

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    city = "London"
    get_current_weather(api_key, city)
    get_weather_forecast(api_key, city)

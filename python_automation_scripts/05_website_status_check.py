import requests
import time

url = "https://example.com"
while True:
    r = requests.get(url)
    status = "UP" if r.status_code == 200 else "DOWN"
    print(f"{url} is {status} - {r.status_code}")
    time.sleep(60)
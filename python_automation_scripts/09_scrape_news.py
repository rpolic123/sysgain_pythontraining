import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, 'html.parser')

for idx, item in enumerate(soup.select('.titleline'), 1):
    print(f"{idx}. {item.text}")
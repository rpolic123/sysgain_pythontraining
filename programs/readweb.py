
###### web scrapping #######
#step1
import requests 
from bs4 import BeautifulSoup
try:
    url = "https://www.google.com/"
    response = requests.get(url)
    if response.status_code == 200 :
        content = response.text
        #print(content)
        #step2 : read the content from html using beautifulsoup library
        soup = BeautifulSoup(content, 'html.parser')

        for link in soup.find_all('a'):
            print(link.get('href'))
            print("-----------")
except Exception as err:
    print(err)





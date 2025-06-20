import requests
import os

urls = ['https://example.com/file1.txt', 'https://example.com/file2.txt']
os.makedirs('downloads', exist_ok=True)

for url in urls:
    filename = os.path.join('downloads', url.split('/')[-1])
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded: {filename}")
import requests
from bs4 import BeautifulSoup

URL = 'https://blog.python.org/'
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h3', class_='post-title')

    print("Recent Blog Post Titles:")
    for title in titles:
        print("-", title.get_text(strip=True))
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")

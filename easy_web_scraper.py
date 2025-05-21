import requests
from bs4 import BeautifulSoup

def scrape_website(url, tag, class_name=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)

        print(f"\nContent found for <{tag} class='{class_name}'>:")
        for el in elements:
            print("-", el.get_text(strip=True))
    
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

scrape_website('https://blog.python.org/', 'h3', 'post-title')

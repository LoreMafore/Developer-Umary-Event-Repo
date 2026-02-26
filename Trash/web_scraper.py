import requests
from bs4 import BeautifulSoup
import time

# Trying to build a web scraper but keep getting blocked
# Need to add better error handling

BASE_URL = "https://example.com"

def fetch_page(url):
    """Fetch a webpage"""
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    try:
        response = requests.get(url, headers=headers)
        # TODO: check status code properly
        return response.text
    except:
        # FIXME: too broad exception handling
        print("Error fetching page")
        return None

def parse_data(html):
    """Parse HTML content"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # TODO: figure out the correct selectors
    # titles = soup.find_all('h2', class_='title')
    
    # for title in titles:
    #     print(title.text)
    
    pass  # placeholder

def scrape_all_pages():
    """Scrape multiple pages"""
    for page_num in range(1, 10):
        url = f"{BASE_URL}/page/{page_num}"
        html = fetch_page(url)
        
        if html:
            parse_data(html)
            time.sleep(1)  # Is 1 second enough? Don't want to get banned
        
        # TODO: save results to file or database

if __name__ == "__main__":
    # scrape_all_pages()  # commented out - still debugging
    print("Scraper not ready yet")

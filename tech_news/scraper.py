from bs4 import BeautifulSoup
import requests
from time import sleep

headers = {"user-agent": "Fake user-agent"}


def fetch(url):
    sleep(1)
    try:
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news = soup.find_all("a", {"class": "cs-overlay-link"})
    urls = []
    for url in news:
        urls.append(url['href'])
    
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

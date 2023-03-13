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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

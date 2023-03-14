from bs4 import BeautifulSoup
from tech_news.database import create_news
import requests
from time import sleep
import re

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
        urls.append(url["href"])

    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    try:
        link = soup.find("a", {"class": "next"})["href"]
        return link
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    url = soup.find('link', attrs={"rel": "canonical"})['href']
    title = soup.find('h1', {'class': 'entry-title'}).text.strip()
    timestamps = soup.find('li', {'class': 'meta-date'}).text
    writer = soup.find('a', {'class': 'url'}).text
    reading_time = soup.find('li', {'class': 'meta-reading-time'}).text
    summary = soup.find('p').text.strip()
    category = soup.find('span', {'class': 'label'}).text
    return {
        'url': url,
        'title': title,
        'timestamp': timestamps,
        'writer': writer,
        'reading_time': int(re.findall('[0-9]+', reading_time)[0]),
        'summary': summary,
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    response = 'https://blog.betrybe.com/'
    fetch_url = response
    true_or_false = True
    list_news = []
    while true_or_false:
        res = fetch(fetch_url)
        urls = scrape_updates(res)
        fetch_url = scrape_next_page_link(res)
        for url in urls:
            if len(list_news) < amount:
                new = fetch(url)
                list_news.append(scrape_news(new))
            else:
                true_or_false = False
                break
    create_news(list_news)
    return list_news


# get_tech_news(10)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


class Newspaper:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f'Newspaper located at {self.url}'

    def __scrape__(self, url):
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')

        return bs


class HarvardBusinessReview(Newspaper):
    def __init__(self):
        super().__init__("https://hbr.org")

    @staticmethod
    def get_available_links(suffix='most-popular'):
        html = urlopen(f'https://hbr.org/{suffix}')
        bs = BeautifulSoup(html.read(), 'html.parser')

        found = bs.find_all('stream-item', {'class': 'stream-item'})
        articles = []
        for item in found:
            link = 'https://hbr.org' + item.find('a')['href']
            articles.append(link)

        return articles


class Space(Newspaper):
    def __init__(self):
        super().__init__("https://www.space.com")

    @staticmethod
    def get_available_links(suffix='spaceflight'):
        html = urlopen(f'https://www.space.com/{suffix}')
        bs = BeautifulSoup(html.read(), 'html.parser')

        found = bs.find_all('a', {'class': {'article-link'}})
        articles = []
        for item in found:
            link = item['href']
            articles.append(link)

        return articles

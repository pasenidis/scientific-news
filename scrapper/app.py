from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from utils import create_article

art = ["https://hbr.org/sponsored/2020/11/how-ai-is-helping-companies-make-deeper-human-connections",
       "https://hbr.org/2020/11/how-biden-won-back-enough-of-the-white-working-class",
       "https://www.space.com/news/live/spacex-crew-1-mission-updates",
       ]


for l in art:
    html = urlopen(l)
    bs = BeautifulSoup(html.read(), 'html.parser')

    if "hbr.org" in l:
        title_tag = bs.find('h1')
        title_tag = title_tag.get_text().strip()

        article = bs.find('div', {'class': 'article-first-row'})
        paragraphs = article.findChildren()

        image = bs.find_all('img', {'src': True, 'class': {
            'alignnone', 'size-full'}})

        for img in image:
            if img is not None:
                src = img["src"]
                image = f'https://hbr.org{src}'

        text = ""
        for p in paragraphs:
            if p.get_text() is not None:
                text += f'{p.get_text().strip()}\n'

        create_article((title_tag, text, "Harvard Business Review", image))

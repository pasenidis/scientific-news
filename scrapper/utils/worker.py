from loguru import logger
from datetime import date
from utils import db_handler, create_article, select_article
from .feed import parse_link


@db_handler
def worker(articles):
    for l in articles:
        logger.info(f"Parsing {l}")

        a = parse_link(l)

        db_data = (a['name'], a['text'], a['source'],
                   a['top_image'], date.today().strftime("%B %d, %Y"))

        if len(select_article(a['name'])) >= 1:
            logger.info('Found an already existing article. Skipping..')
            continue
        else:
            logger.info(f"Pushing to database")
            create_article(db_data)

        logger.success('Finished a task.')

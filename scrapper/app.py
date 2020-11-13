from utils import (
    create_table,
    create_article,
    select_article,
    parse_link,
    db_handler,
    worker
)
from newspapers import HarvardBusinessReview, Space
from pyfiglet import figlet_format
from sqlite3 import OperationalError
from datetime import date
from loguru import logger
from json import load


CONFIG_PATH = "config.json"


def main():
    """Run this to start the microservice."""

    config = load_json(CONFIG_PATH)

    logger.add(config['logs']['output_name'], format="{time} {level} {message}",
               level=config['logs']['level'])

    greet()  # print a greeting message to the users
    process_links(config['domains'])

    logger.success('All done. Check for the changes in your DB!')


def process_links(domains):
    """Parse articles"""
    from newspaper import Article

    links = []

    for d in domains:
        if "hbr.org" in d:
            links.extend(
                HarvardBusinessReview.get_available_links('most-popular'))
        elif "space.com" in d:
            links.extend(
                Space.get_available_links('spaceflight')
            )
            links.extend(
                Space.get_available_links('tech-robots')
            )

    worker(links)  # loop through the links to add them to the DB


def greet():
    """Printing greetings at script start-up."""
    name = 'Scientific News'
    messages = [
        'Made by:',
        'Edward Pasenidis, Nikos Ntiakakis & Tasos Meletlidis\n\n'
        'Source: https://git.io/JkYGb\n\n',
        'You can run this microservice as a CRON job or anything else you want.\n\n'
    ]
    print(figlet_format(name, font='slant'))

    for t in messages:
        print(t)


def load_json(path):
    """Load JSON files to parse the configuration"""
    with open(path) as j:
        data = load(j)
        return data


if __name__ == "__main__":
    main()
else:
    print('Using this file as an imported module. \nPlease be extremely cautious!')

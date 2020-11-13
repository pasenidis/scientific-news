from utils import (
    create_table,
    create_article,
    select_article,
    parse_link,
    db_handler,
    worker
)
from pyfiglet import figlet_format
from sqlite3 import OperationalError
from datetime import date
from loguru import logger
from json import load

art = ["https://hbr.org/sponsored/2020/11/how-ai-is-helping-companies-make-deeper-human-connections",
       "https://hbr.org/2020/11/how-biden-won-back-enough-of-the-white-working-class",
       "https://www.space.com/news/live/spacex-crew-1-mission-updates",
       ]

CONFIG_PATH = "config.json"


def main():
    """Run this to start the microservice."""

    config = load_json(CONFIG_PATH)

    logger.add(config['logs']['output_name'], format="{time} {level} {message}",
               level=config['logs']['level'])

    greet()  # print a greeting message to the users
    worker(art)  # loop through the links to add them to the DB
    logger.success('All done. Check for the changes in your DB!')


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

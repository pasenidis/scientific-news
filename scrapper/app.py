from utils import create_table, create_article, parse_link
from pyfiglet import figlet_format
from sqlite3 import OperationalError
from datetime import date
from loguru import logger

art = ["https://hbr.org/sponsored/2020/11/how-ai-is-helping-companies-make-deeper-human-connections",
       "https://hbr.org/2020/11/how-biden-won-back-enough-of-the-white-working-class",
       "https://www.space.com/news/live/spacex-crew-1-mission-updates",
       ]


def main():
    """Run this to start the microservice."""

    logger.add("debug.log", format="{time} {level} {message}",
               level="DEBUG")

    greet()  # print a greeting message to the users

    # loop through the links to add them to the DB
    for l in art:
        logger.info(f"Parsing {l}")

        a = parse_link(l)

        db_data = (a['name'], a['text'], a['source'],
                   a['top_image'], date.today().strftime("%B %d, %Y"))

        try:
            logger.info(f"Pushing to database")
            create_article(db_data)
        except OperationalError as e:
            if "no such table" in str(e):
                logger.warning(
                    "Tables are not initialized. Running SQL queries...")

                query = """
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER NOT NULL PRIMARY KEY,
                    name TEXT NOT NULL,
                    content TEXT NOT NULL,
                    image TEXT NOT NULL,
                    source TEXT NOT NULL,
                    date TEXT NOT NULL
                );
                """
                create_table(query)
                create_article(db_data)

        logger.success('Finished a task.')
    logger.success('All done. Check for the changes in your DB!')


def greet():
    """Printing greetings at script start-up."""
    name = 'Scientific News'
    messages = [
        'Made by:',
        'Edward Pasenidis, Nikolakis Ntiakakis & Tasos Meletlidis\n']
    print(figlet_format(name, font='slant'))

    for t in messages:
        print(t)


if __name__ == "__main__":
    main()
else:
    print('Using this file as an imported module. \nPlease be extremely cautious!')

from sqlite3 import OperationalError
from loguru import logger
from utils import create_table


def exc_handler(func):

    def worker(*args, **kwargs):
        try:
            func(*args, **kwargs)
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
                logger.warning('Restarting script...')
                func(*args, **kwargs)

    return worker

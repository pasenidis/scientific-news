import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a DB connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """Create a DB table"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_article(article):
    """Craate an article"""

    sql = """ INSERT INTO article(name, content, source, image, date)
              VALUES(?,?,?,?,?)"""

    conn = create_connection('hahaha.db')
    cur = conn.cursor()
    cur.execute(sql, article)
    conn.commit()
    return cur.lastrowid


def main():
    db_path = r"C:\folder\db.db"

    sqL_create_articles_table = """ CREATE TABLE IF NOT EXISTS articles (
                id integer PRIMARY_KEY,
                name text NOT NULL,
                content text NOT NULL,
                image text NOT NULL,
                source text NOT NULL,
                date text NOT NULL,
            );"""

    if conn := create_connection(db_path) is not None:
        create_table(conn, sqL_create_articles_table)


if __name__ == "__main__":
    create_connection(r"C:\path\to\db.db")

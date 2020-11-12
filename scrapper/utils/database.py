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


def create_table(create_table_sql):
    """Create a DB table"""
    try:
        conn = create_connection("../database/data.db")
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_article(article):
    """Craate an article"""

    sql = """ INSERT INTO articles(name, content, source, image, date)
              VALUES(?,?,?,?,?)"""

    conn = create_connection('../database/data.db')
    cur = conn.cursor()
    cur.execute(sql, article)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    print('database.py is not supposed to be ran as a file. \nUse it as a module instead')
    exit(1)
else:
    print('database module is initialized.')

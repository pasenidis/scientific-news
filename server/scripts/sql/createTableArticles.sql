CREATE TABLE IF NOT EXISTS articles (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    content TEXT NOT NULL,
    image TEXT NOT NULL,
    source TEXT NOT NULL,
    date TEXT NOT NULL
);
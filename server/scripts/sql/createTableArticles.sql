CREATE TABLE IF NOT EXISTS articles (
    id integer PRIMARY_KEY,
    name text NOT NULL,
    content text NOT NULL,
    image text NOT NULL,
    source text NOT NULL,
    date text NOT NULL
);
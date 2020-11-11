CREATE TABLE IF NOT EXISTS articles (
    id int PRIMARY KEY,
    name text NOT NULL,
    content text NOT NULL,
    image text NOT NULL,
    source text NOT NULL,
    date text NOT NULL
);
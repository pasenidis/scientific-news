# Scientific News / Scrapper

## Configuration
In order for the script to work properly, you must create a config.json

```sh
cp config.json.example config.json
```

- `db.name` is the name of the SQL table that will contain the articles (this is the one that will be fetched with Express)
- `logs.output_name` is the name of the log file
- `logs.level` is the logs level (default is DEBUG, better leave it like that)
- `domains` is an array / list / whatever it is called in your language, it contains domains from newspapers that will be scanned.
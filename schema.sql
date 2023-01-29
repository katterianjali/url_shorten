DROP TABLE IF EXISTS url_table;

CREATE TABLE url_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    hash_id TEXT
);
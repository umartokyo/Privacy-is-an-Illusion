DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT NOT NULL,
    ip_version TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL,
    country TEXT NOT NULL,
    latitude INT NOT NULL,
    longitude INT NOT NULL,
    postal TEXT NOT NULL,
    org TEXT NOT NULL
)
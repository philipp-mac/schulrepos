CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name text,
    guesses INTEGER NOT NULL,
    correctnumber INTEGER
);

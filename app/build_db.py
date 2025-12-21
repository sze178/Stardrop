# S.T.A.R.D.R.O.P // Stardrop
# Roster: Alvin Sze, Kiran Soemardjo, James Sun, Jalen Chen
# SoftDev

import sqlite3

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript("""
DROP TABLE IF EXISTS players;
CREATE TABLE players (
    username TEXT PK,
    name TEXT,
    password TEXT,
    money REAL DEFAULT 0,
    santa_opinion INTEGER DEFAULT 0,
    cowboy_opinion INTEGER DEFAULT 0,
    pirate_opinion INTEGER DEFAULT 0,         
    supplies TEXT,
    time_period DATETIME,
    alcohol_on BOOLEAN DEFAULT TRUE
);
""")

db.commit()
db.close()
import sqlite3


DB_FILE_NAME = "data.db"
SQL_FILE_NAME = "create_db.sql"

CONN = sqlite3.connect(DB_FILE_NAME)
CUR = CONN.cursor()

DATA = {
    "Weapons": {
        "records": 20,
        "name": "Weapon-{}",
        "params": 5,
        "query": "INSERT INTO Weapons VALUES (?, ?, ?, ?, ?, ?)"
    },
    "Hulls": {
        "records": 5,
        "name": "Hull-{}",
        "params": 3,
        "query": "INSERT INTO Hulls VALUES (?, ?, ?, ?)"
    },
    "Engines": {
        "records": 6,
        "name": "Engine-{}",
        "params": 2,
        "query": "INSERT INTO Engines VALUES (?, ?, ?)"
    },
    "Ships": {
        "records": 200,
        "name": "Ship-{}",
        "params": 3,
        "query": "INSERT INTO Ships VALUES (?, ?, ?, ?)",
    }
}

KEYS = tuple(DATA.keys())
MAX_INT = 20

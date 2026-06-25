import os
import sqlite3
from pathlib import Path

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/inventory.db")


def get_database_path() -> Path:
    if not DATABASE_URL.startswith("sqlite:///"):
        raise ValueError("Only SQLite database URLs are supported.")

    return Path(DATABASE_URL.replace("sqlite:///", "", 1))


def get_connection() -> sqlite3.Connection:
    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db() -> None:
    """Create the local SQLite schema when the API starts."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL CHECK (price >= 0),
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

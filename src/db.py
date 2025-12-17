import sqlite3
import pandas as pd

def run_query(query: str, db_path: str = "data/database.sqlite") -> pd.DataFrame:
    """Run a SQL query on the SQLite database and return a DataFrame."""
    with sqlite3.connect(db_path) as con:
        return pd.read_sql_query(query, con)

def list_tables(db_path: str = "data/database.sqlite") -> pd.DataFrame:
    """List all tables in the SQLite database."""
    q = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    return run_query(q, db_path)

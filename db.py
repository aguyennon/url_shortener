import sqlite3


def get_connection():
    conn = sqlite3.connect("urls.db")

    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- the database hands out 1, 2, 3... by itself
                long_url TEXT NOT NULL                 -- the original link, never allowed to be empty
            )
            """
        )
    conn.close()

init_db()

def save_url(long_url):
    conn = get_connection()
    conn_cursor = conn.cursor() # object that sends sql to db and holds what comes back
    conn_cursor.execute(
        """
        INSERT INTO urls (long_url) VALUES (?)
        """,
        (long_url,) # comma to make it a tuple ( to hold the value replacing the ? )
    )
    new_id = conn_cursor.lastrowid 
    conn.commit()
    conn.close()

    return new_id


def get_url(url_id):
    conn = get_connection()
    conn_cursor = conn.cursor()
    conn_cursor.execute(
        """
        SELECT long_url FROM urls WHERE id = ?
        """,
        (url_id,)
    )
    row = conn_cursor.fetchone()
    conn.close()

    return None if row is None else row[0]


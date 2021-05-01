import sqlite3
import datetime

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY,
                time REAL,
                category TEXT,
                label TEXT,
                content TEXT
);"""


INSERT_NOTE = """INSERT INTO note (time, category, label, content) 
                VALUES(?,?, ?,?);"""

DISPLAY_NOTE = "SELECT * FROM note"

SEARCH_CATEGORY = "SELECT * FROM note WHERE category = ?;"

SEARCH_LABEL = "SELECT * FROM note WHERE label = ?;"

SEARCH_KEYWORD = "SELECT * FROM note WHERE content LIKE ?;"

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(CREATE_TABLE)
    
def note(cat, lab, content):
    with connection:
        today_timestamp = datetime.datetime.today().timestamp()
        today = datetime.datetime.fromtimestamp(today_timestamp)
        human_date = today.strftime("%Y/%m/%d")
        connection.execute(INSERT_NOTE, (human_date, cat, lab, content))

def display():
    with connection:
        cursor = connection.cursor()
        cursor.execute(DISPLAY_NOTE)
        return cursor.fetchall()

def search_cat(cat):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_CATEGORY,(cat,))
        return cursor.fetchall()

def search_lab(lab):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_LABEL, (lab,))
        return cursor.fetchall()

def search_keyword(keyword):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_KEYWORD, (f"% {keyword} %",))
        return cursor.fetchall()


import sqlite3


CREATE_TABLE = """CREATE TABLE IF NOT EXISTS note (
                category TEXT,
                label TEXT,
                content TEXT
);"""

INSERT_NOTE = "INSERT INTO note VALUES(?,?,?);"

DISPLAY_NOTE = "SELECT * FROM note;" 

SEARCH_CATEGORY = "SELECT * FROM note WHERE category = ?;"

SEARCH_LABEL = "SELECT * FROM note WHERE label = ?;"

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(CREATE_TABLE)

def note(cat, lab, content):
    with connection:
        connection.execute(INSERT_NOTE, (cat, lab, content))

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

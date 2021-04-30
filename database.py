import sqlite3


CREATE_NOTE_TABLE = """CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY,
                time REAL
                content TEXT
);"""

CREATE_CATEGORY_TABLE = """CREATE TABLE IF NOT EXISTS categories (
                category TEXT
);"""

CREATE_LABEL_TABLE = """CREATE TABLE IF NOT EXISTS labels (
                        label TEXT,
);"""

INSERT_NOTE = "INSERT INTO note (time, content) VALUES(?,?);"

INSERT_CATEGORY = "INSERT INTO categories VALUES(?);"

INSERT_LABEL = "INSERT INTO labels VALUES(?);"

DISPLAY_NOTE = """SELECT * FROM category
JOIN note ON ;

""" 

SEARCH_CATEGORY = "SELECT * FROM note WHERE category = ?;"

SEARCH_LABEL = "SELECT * FROM note WHERE label = ?;"

SEARCH_NOTE = "SELECT * FROM note WHERE content LIKE ?;"

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute(CREATE_NOTE_TABLE)
        connection.execute(CREATE_CATEGORY_TABLE)
        connection.execute(CREATE_LABEL_TABLE)
    
def note(content):
    with connection:
        today_timestamp = datetime.datetime.today().timestamp()
        connection.execute(INSERT_NOTE, (today_timestamp, content))

def category(category):
    with connection:
        connection.execute(INSERT_CATEGORY,(category,)) 

def label(lab):
    with connection:
        connection.execute(INSERT_LABELE, (lab,))

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

def search_note(keyword):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_NOTE, (f"% {keyword} %",))
        return cursor.fetchall()

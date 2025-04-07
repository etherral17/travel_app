import sqlite3

DB_NAME = "travel.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS consumers
                 (name TEXT, email TEXT, package TEXT)''')
    conn.commit()
    conn.close()

def insert_consumer(name, email, package):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO consumers VALUES (?, ?, ?)", (name, email, package))
    conn.commit()
    conn.close()

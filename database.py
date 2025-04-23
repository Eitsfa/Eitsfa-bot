import sqlite3

def init_db():
    conn = sqlite3.connect('eitsfa.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)''')
    conn.commit()
    conn.close()
import sqlite3
import Model

class database:
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Files (
                            ID INTEGER PRIMARY KEY,
                            firstname TEXT,
                            lastname TEXT,
                            gmail TEXT
                            password TEXT,
                            confirmpassword TEXT,
                            day INTEGER,
                            month INTEGER,
                            year INTEGER
                        )''')
        self.conn.commit()

    
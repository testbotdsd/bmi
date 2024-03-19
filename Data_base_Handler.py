import sqlite3
import Model

class database:
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.Sign_up_table = 'sign_up_table'
        self.cursor = self.conn.cursor()


        create_sign_up_table = f'''CREATE TABLE IF NOT EXISTS {self.Sign_up_table} (
                            ID INTEGER PRIMARY KEY,
                            firstname TEXT,
                            lastname TEXT,
                            gmail TEXT,
                            username TEXT,
                            password TEXT,
                            birthday TEXT
                        )'''
        
        self.conn.execute(create_sign_up_table)

        self.conn.commit()
        
        
    def create_sign_up_table (self, user:Model.User):
        query = f"INSERT INTO {self.Sign_up_table} (firstname, lastname, gmail,username , password, birthday) VALUES (?,?,?,?,?,?)" 
        values = (user.firstname, user.lastname, user.gmail, user.username, user.password, user.birthday)
        self.cursor.execute(query, values) 
        self.conn.commit()

    def check_credentials(self, username, password):
        query = f"SELECT * FROM {self.Sign_up_table} WHERE username=? AND password=?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        return user is not None
            
        
        

    
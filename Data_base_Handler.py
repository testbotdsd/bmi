import sqlite3
import Model

class database:
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.Sign_up_table = 'sign_up_table'
        self.Save_info_table = 'save_info_table'
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

        create_save_info_table = f'''CREATE TABLE IF NOT EXISTS {self.Save_info_table} (
                                    ID INTEGER PRIMARY KEY,
                                    age INTEGER,
                                    kilogram INTEGER,
                                    pounds INTEGER,
                                    centimeter INTEGER,
                                    meter INTEGER,
                                    user_id INTEGER,
                                    FOREIGN KEY (user_id) REFERENCES {self.Sign_up_table}(ID)
                                )'''

        self.conn.execute(create_save_info_table)
        self.conn.commit()

    def create_save_info_table(self, Input: Model.Save_info, user_id):
        query = f"INSERT INTO {self.Save_info_table} (age, kilogram, pounds, centimeter, meter, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        values = (Input.age, Input.kilogram, Input.pounds, Input.centimeter, Input.meter, user_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        
<<<<<<< HEAD
    def create_sign_up_table(self, User: Model.User):
=======
        
    def create_sign_up_table (self, user:Model.User):
>>>>>>> fdabfb0a6f4324411e891e0863cef9a68b72fbfd
        query = f"INSERT INTO {self.Sign_up_table} (firstname, lastname, gmail,username , password, birthday) VALUES (?,?,?,?,?,?)" 
        values = (user.firstname, user.lastname, user.gmail, user.username, user.password, user.birthday)
        self.cursor.execute(query, values) 
        self.conn.commit()

    def check_credentials(self, username, password):
        query = f"SELECT * FROM {self.Sign_up_table} WHERE username=? AND password=?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        if user:
            return user[0] 
        else:
            return None
        
    
        
        

    
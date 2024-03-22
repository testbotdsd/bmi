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
                            gmail TEXT UNIQUE,
                            username TEXT,
                            password TEXT,
                            birthday TEXT,
                            image BLOB
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
        
    def get_Bmilist(self):
        query = f"SELECT id, age,kilogram, pounds, centimeter,meter FROM {self.Save_info_table}"
        self.cursor.execute(query)
        
        BMI=[]

        for row in self.cursor:
            new_bmi_info=Model.Save_info() 
            new_bmi_info.Id= row[0]
            new_bmi_info.age=row[1]
            new_bmi_info.kilogram=row[2]
            new_bmi_info.pounds=row[3]
            new_bmi_info.centimeter=row[4]
            new_bmi_info.meter=row[5]
            BMI.append(new_bmi_info)

        return BMI

    def create_save_info_table(self, Input: Model.Save_info, user_id):
        query = f"INSERT INTO {self.Save_info_table} (age, kilogram, pounds, centimeter, meter, user_id) VALUES (?, ?, ?, ?, ?, ?)"
        values = (Input.age, Input.kilogram, Input.pounds, Input.centimeter, Input.meter, user_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def create_sign_up_table(self, User: Model.User):
        query = f"INSERT INTO {self.Sign_up_table} (firstname, lastname, gmail,username , password, birthday, image) VALUES (?,?,?,?,?,?,?)" 
        values = (User.firstname, User.lastname, User.gmail, User.username, User.password, User.birthday, User.image)
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
        
    def read_Bmi(self, id:int):
        query = f"SELECT * FROM {self.Save_info_table} WHERE id=?"
        values = (id,)
        self.cursor.execute(query, values)

        BMI = []

        for row in self.cursor:
            BMI = Model.Save_info()
            BMI.id = row[0]
            BMI.age = row[1]
            BMI.kilogram=row[2]
            BMI.pounds=row[3]
            BMI.centimeter=row[4]
            BMI.meter=row[5]

        return BMI
        
    def delete_Bmi_history(self,bmi: int):
        query=f"DELETE FROM {self.Save_info_table} WHERE id =?"
        values=(bmi,)
        self.cursor.execute(query,values)
        self.conn.commit()  

    def checking_gmail_exist(self, gmail):
        query = f"SELECT COUNT(*) FROM {self.Sign_up_table} WHERE gmail = ?"
        self.cursor.execute(query, (gmail,)) 
        result = self.cursor.fetchone()
        return result[0] > 0

    def update_password(self, gmail, password):
        query = f"UPDATE {self.Sign_up_table} SET password=? WHERE gmail = ?"
        values = (password, gmail)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_profile_image(self, user_id):
        query = f"SELECT image FROM sign_up_table WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def get_user_info(self, user_id):
        query = f"SELECT firstname, lastname, gmail, username, birthday FROM {self.Sign_up_table} WHERE ID = ?"
        self.cursor.execute(query, (user_id,))
        user_info = self.cursor.fetchone()
        return user_info

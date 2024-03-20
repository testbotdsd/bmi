import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
import random
import string
from tkcalendar import DateEntry
from datetime import date
import sqlite3
from PIL import Image, ImageTk


# Model
class User:
    def __init__(self):
        self.Id = 0
        self.firstname = ''
        self.lastname = ''
        self.gmail = ''
        self.username = ''
        self.password = ''
        self.birthday = ''
        
class Save_info:
    def __init__(self):
        self.Id = 0
        self.age = 0
        self.kilogram = 0
        self.pounds = 0
        self.centimeter = 0
        self.meter = 0

# Database Handler
class Database:
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

    def create_save_info_table(self, Input:Save_info):
        query = f"INSERT INTO {self.Save_info_table} (age, kilogram, pounds, centimeter,meter) VALUES(?,?,?,?,?)"
        Values = (Input.age, Input.kilogram, Input.pounds, Input.centimeter, Input.meter)
        self.cursor.execute(query, Values)
        self.conn.commit()
        
    def create_sign_up_table (self, User:User):
        query = f"INSERT INTO {self.Sign_up_table} (firstname, lastname, gmail,username , password, birthday) VALUES (?,?,?,?,?,?)" 
        values = (User.firstname, User.lastname, User.gmail, User.username, User.password, User.birthday)
        self.cursor.execute(query, values) 
        self.conn.commit()

    def check_credentials(self, username, password):
        query = f"SELECT * FROM {self.Sign_up_table} WHERE username=? AND password=?"
        self.cursor.execute(query, (username, password))
        user = self.cursor.fetchone()
        return user is not None
            

# Sign Up Page
class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=450, height=600)


        #WELCOME LABELS
        self.create_account_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.create_account_bg.place(x=0, y=0)

        self.create_account_label = tk.Label(self, text='Create an Account', font=('Courier', 25, 'bold'),  fg='#EEEDEB', bg='#3C3633')
        self.create_account_label.place(x=55, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font=('Courier', 15, 'bold'),   fg='#EEEDEB', bg='#3C3633')
        self.to_get_started_label.place(x=130, y=50)

        #INFORMATIONS
        self.first_name_label = tk.Label(self, text='First Name', font=('Courier', 13),  fg='#EEEDEB', bg='#3C3633')
        self.first_name_label.place(x=45, y=120)

        self.first_name_entry = tk.Entry(self, border=1, font=('Courier', 13), width=17, bg='#59504b')
        self.first_name_entry.place(x=42, y=144)

        self.last_name_label = tk.Label(self, text='Last Name', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.last_name_label.place(x=235, y=120)

        self.last_name_entry = tk.Entry(self, border=1, font=('Courier', 13),width=17, bg='#59504b')
        self.last_name_entry.place(x=237, y=144)

        self.gmail_label = tk.Label(self, text='Gmail', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.gmail_label.place(x=100, y=246)

        self.gmail_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.gmail_entry.place(x=100, y=270)

        self.username_label = tk.Label(self, text='Username', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=100, y=303)

        self.username_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.username_entry.place(x=100, y=327)

        self.password_label = tk.Label(self, text='Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.password_label.place(x=100, y=360)
        
        self.password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b', show="*")
        self.password_entry.place(x=100, y=384)

        self.confirm_password_label = tk.Label(self, text='Confirm Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.confirm_password_label.place(x=100, y=420)

        self.confirm_password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b', show="*")
        self.confirm_password_entry.place(x=100, y = 444)

        self.birthday_label = tk.Label(self, text = 'Birthday', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=100, y=189) 
    
        self.Bday_calendar_entry = DateEntry(self,width=35,background='Grey', foreground='white', borderwidth=2)
        self.Bday_calendar_entry.place (x=100, y=213)
        
        self.clear_button = tk.Button(self, text='Clear', width=10, font=('Courier', 15, 'bold'),bg='#d3d3d3', command=self.clear_input)
        self.clear_button.place(x=90, y=500)

        self.toggle_password_button = tk.Button(self, text="Show", font=('Courier', 10), bd=1, bg='white',fg='black', command=self.toggle_password)
        self.toggle_password_button.place(x=350, y=415)

        self.have_an_account_login_label = tk.Label(self, text='Already have an account?', bg='#3C3633', font="Courier 10", foreground='white')
        self.have_an_account_login_label.place(x=100, y=560)

        self.sign_up_button = tk.Button(self, text='Continue', width=10, font=('Courier', 15, 'bold'),bg='#d3d3d3', command=self.validate_sign_up)
        self.sign_up_button.place(x=225, y=500)
        
        self.login_clickable = tk.Button(self, text="Log in", fg='#EEEDEB', bg='#3C3633' , bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.login_clickable.place(x=295, y=559)

        self.password_hidden = True 

    def toggle_password(self):
        if self.password_hidden:
            self.password_entry.config(show='')
            self.confirm_password_entry.config(show='')
            self.toggle_password_button.config(text="Hide", bg='#3C3633', fg='white')
            self.password_hidden = False
        else:
            self.password_entry.config(show='*')
            self.confirm_password_entry.config(show='*')
            self.toggle_password_button.config(text="Show", bg='white', fg='#3C3633')
            self.password_hidden = True

    def clear_input(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.gmail_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.Bday_calendar_entry.delete (0, tk.END)
        
    def validate_sign_up(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gmail = self.gmail_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        birthday = self.Bday_calendar_entry.get()
        chosen_date = date.today()
        
        if first_name == '':
            messagebox.showerror('Error', 'First name field is empty, please fill it out.')
            return False
        
        if last_name == '':
            messagebox.showerror('Error', 'Last name field is empty, please fill it out.')
            return False
        
        if gmail == '':
            messagebox.showerror('Error', 'Gmail field is empty, please fill it out.')
            return False
        
        if username == '':
            messagebox.showerror('Error', 'Username field is empty, please fill it out.')
            return False
        
        if password == '':
            messagebox.showerror('Error', 'Password field is empty, please fill it out.')
            return False
        
        if confirm_password == '':
            messagebox.showerror('Error', 'Confirm password field is empty, please fill it out.')
            return False
        
        if birthday == '':
            messagebox.showerror('Error', 'Birthday password field is empty, please fill it out.')
            return False
        
        if chosen_date > date.today():
            messagebox.showerror('Error', 'Birth Date is beyond the current date, Please put your real birthday')
            return False
        
        self.go_to_Photo_page()

        
    def clear_input(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.gmail_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.Bday_calendar_entry.delete(0, tk.END)
        
    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')

    def go_to_Photo_page(self):
        self.parent.change_window('Photo')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')
        
    def on_return(self):
        pass
    
class Photo (tk.Frame):
    def __init__(self, master, signup_frame):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.signup_frame = signup_frame
        self.config(width=400, height=600)
        
        self.Photo_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.Photo_bg.place(x=0, y=0)
        
        self.pic_frame = tk.Frame(self, bd=10, width=150, height=150, bg='white', relief='flat')
        self.pic_frame.place(x=125, y=70)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = tk.Button(self, text='Sign Up', width=21, font=('Courier', 15, 'bold'), bg='#d3d3d3', command=self.go_to_Login_Page)
        self.Finish_button.place(x=65, y=517)
        
        self.captcha_label = tk.Label(self, text='Captcha', font=('Courier', 12, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.captcha_label.place(x=160, y=255)

        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self.Photo_bg, text="I accept the Terms and Conditions", variable=self.terms_and_conditions_var, bg='#3C3633', fg="white")
        self.terms_and_conditions_check_button.place(x=95, y=484)

        self.generate_captcha_button = tk.Button(self, text="Generate Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3', command=self.generate_captcha)
        self.generate_captcha_button.place(x=110, y=290)

        self.captcha_label = tk.Label(self, text='', font=("Arial", 12), width=10, bg='#59504b')
        self.captcha_label.place(x=150, y=335)
            
        self.captcha = tk.Label(self, text="Enter Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3')
        self.captcha.place(x=130, y=390)
        self.captcha_input = tk.Entry(self, text="Enter Captcha here", width=20, bg='#59504b')
        self.captcha_input.place(x=135, y=425)

    def generate_captcha(self):
        captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6,))
        self.captcha_label.config(text=captcha)

    def terms_conditios_var(self):
        if self.terms_and_conditions_var.get():
            result = messagebox.askokcancel("Terms and condition", "Do you accept the Terms and Conditions?")
            if result:
                 pass
            else:
                self.terms_and_conditions_var.set(False)
        
    def go_to_create_acc(self):
        self.parent.change_window('Signup')
        
    def go_to_Login_Page(self):
        FName = self.signup_frame.first_name_entry.get().strip()
        LName = self.signup_frame.last_name_entry.get().strip()
        Uname = self.signup_frame.username_entry.get().strip()
        Bday = self.signup_frame.Bday_calendar_entry.get().strip()
        Gmail = self.signup_frame.gmail_entry.get().strip()
        Pass = self.signup_frame.password_entry.get().strip()
        Confirm_Pass = self.signup_frame.confirm_password_entry.get().strip()

        user = User()  # Corrected to User
        user.firstname = FName
        user.lastname = LName
        user.username = Uname
        user.birthday = Bday
        user.gmail = Gmail
        user.password = Pass
        
        if Pass == Confirm_Pass:
            dbconn = Database()  # Corrected to Database
            dbconn.create_sign_up_table(user)
            user_id = dbconn.cursor.lastrowid  # Get the last inserted ID
            dbconn.conn.close()
            self.save_info(user_id)  # Pass the user_id to save_info method
        else:
            messagebox.showerror("Error", "Incorrect Password.")
            return
        
        final = messagebox.askokcancel('Signup', 'Finish signing up?')
        if final:
            self.parent.frames['Signup'].clear_input()
            self.parent.change_window('Login')
            self.save_info(user_id)  


# Login Page
class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=450, height=600)


        #ANGELAINE NEW
        self.login_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self.login_bg, text="WELCOME", font=('Courier', 45, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.welcome_label.place(x=95, y=40)

        self.username_label = tk.Label(self.login_bg, text="Username", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=81, y=185)

        self.username_entry = tk.Entry(self.login_bg, border=1, width=23, font=('Courier', 15),fg='white', bg='#59504b')
        self.username_entry.place(x=81, y=215)

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.pass_label.place(x=81, y=265)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=19, font=('Courier', 15), fg='white', bg='#59504b', show='*')
        self.pass_entry.place(x=81, y=295)

        self.toggle_password_button = tk.Button(self.login_bg, text="Show", font=('Courier', 10), bd=1, bg='white',fg='black', command=self.toggle_password)
        self.toggle_password_button.place(x=322, y=296)

        self.login_button = CTkButton(self.login_bg, text='LOGIN', width=300,height=40,corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', 
                                        text_color='black',command=self.validate_login)
        self.login_button.place(x=81, y=440)

        self.forgot_password_button = tk.Button(self.login_bg, text='Forgot your password?',  font=('Courier', 11), fg='#5e918e', 
                                                bg='#3C3633', bd=0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=166, y=322)

        self.no_account_label = tk.Label(self.login_bg, text="Don't have an account?", bg='#3C3633', font="Courier 10", foreground='#EEEDEB')
        self.no_account_label.place(x=82, y=488)

        self.sign_up_btn = tk.Button(self.login_bg, text="Sign up now", bg='#3C3633', bd=0, font=('Courier', 10, 'bold'), 
                                        command=self.go_to_signup, foreground='#5e918e')
        self.sign_up_btn.place(x=264, y=487)

        self.password_hidden = True 

    def toggle_password(self):
        if self.password_hidden:
            self.pass_entry.config(show='')
            self.toggle_password_button.config(text="Hide", bg='#3C3633', fg='white')
            self.password_hidden = False
        else:
            self.pass_entry.config(show='*')
            self.toggle_password_button.config(text="Show", bg='white', fg='#3C3633')
            self.password_hidden = True

    def go_to_forgot_password(self):
        self.parent.change_window('Forget')

    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')
    
    def go_to_signup(self):
        self.parent.frames['Signup'].Bday_calendar_entry.delete(0, tk.END)
        self.parent.change_window('Signup')

    def validate_login(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()

        dbconn = Database()  # Corrected here
        if dbconn.check_credentials(username, password):
            self.reset_fields()
            self.go_to_BMI_Page()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")

        dbconn.conn.close()

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
    
    def on_return(self):
        pass

# BMI Page
class BMI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.main_frame = tk.Frame(self, bg='#3C3633', height=600, width=450)

        # TOP FRAMES
        self.frame_top_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        self.frame_top_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        
        # BOTTOM FRAMES
        self.frame_bottom_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        self.frame_bottom_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        
        #Result Frame
        self.frame_result = tk.Frame(self.main_frame, bd=10, width=305, height=60, bg='#747264', relief='flat')

        self.main_frame.place(x=0, y=0)
        self.frame_top_left.place(x=45, y=95)
        self.frame_top_right.place(x=215, y=95)
        self.frame_bottom_left.place(x=45, y=190)
        self.frame_bottom_right.place(x=215, y=190)
        self.frame_result.place(x=45, y=332)
        
        # Age Label and Entry
        self.age_label = tk.Label(self.main_frame, text="Age", bg='#747264', font=("Perpetua", 10, 'bold'), foreground='#E0CCBE')
        self.age_label.place(x=45, y=70)
        self.age_entry = tk.Entry(self.main_frame, width=39, font=("Perpetua", 10), bg='#E0CCBE',)
        self.age_entry.place(x=78, y=70)

        # self.create_account_bg = tk.Frame(self, bg='#DE8971', height=600, width=450)
        # self.create_account_bg.place(x=0, y=0)

        self.menu_img = Image.open("menu_icon.png")
        self.menu_img = self.menu_img.resize((30, 30))
        self.menu_icon = ImageTk.PhotoImage(self.menu_img)
        self.menu_btn = tk.Button(self, image=self.menu_icon, highlightbackground='#DE8971', highlightcolor='#DE8971',
                                  border=0, command=self.got_to_profile_page)
        self.menu_btn.place(x=367, y=0)

        self.welcome_label = tk.Label(self, text="BMI Calculator", bg='#3C3633', font=('Courier', 17, 'bold'), 
                                      foreground='#E0CCBE')
        self.welcome_label.place(x=100, y=10)
        

        # WEIGHT LABEL AND ENTRY
        self.weight_kg_label = tk.Label(self.frame_top_left, text="Weight (kg)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.weight_kg_label.place(x=13,y=0)
        self.weight_lb_label = tk.Label(self.frame_top_right, text="Weight (lb)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.weight_lb_label.place(x=14,y=0)

        self.weight_kg_entry = tk.Entry(self.frame_top_left, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.weight_kg_entry.place(x=15, y=30)
        self.weight_lb_entry = tk.Entry(self.frame_top_right, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.weight_lb_entry.place(x=15, y=30)
        
        self.weight_kg_entry.bind('<KeyRelease>', self.update_weight_lb)
        self.weight_lb_entry.bind('<KeyRelease>', self.update_weight_kg)
        

        # HEIGH LABEL AND ENTRY
        self.height_cm_label = tk.Label(self.frame_bottom_left, text="Height (cm)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.height_cm_label.place(x=13,y=0)
        self.height_m_label = tk.Label(self.frame_bottom_right, text="Height (m)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                       foreground='#E0CCBE')
        self.height_m_label.place(x=18,y=0)

        self.height_cm_entry = tk.Entry(self.frame_bottom_left, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.height_cm_entry.place(x=15, y=30)
        self.height_m_entry = tk.Entry(self.frame_bottom_right, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.height_m_entry.place(x=15, y=30)

        self.submit_button = tk.Button (self.main_frame, text = 'Calculate BMI', cursor='gumby', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", height=1, width=16, command=self.calculate_BMI)
        self.submit_button.place(x=215, y=285)

        self.clear_button = tk.Button(self.main_frame, text = 'Clear', cursor='gumby', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", width=16, command = self.clear_button)
        self.clear_button.place(x=45, y=285)

        self.history_button = tk.Button (self.main_frame, text = 'View History', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", height=1, width=16, command=self.history_info)
        self.history_button.place(x=45, y=480)

        self.save_button = tk.Button(self.main_frame, text='Save', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"),
                                    relief="raised", width=16, command=lambda: self.save_info)

        self.save_button.place(x=215, y=480)
        
        # RESULT
        self.result_label = tk.Label (self.frame_result, text='Your BMI is:', bg='#747264', font=("Perpetua", 13, 'bold'), foreground='#E0CCBE')
        self.result_label.place (x =5, y = 6 )
        
        self.result_entry = tk.Entry(self.frame_result, width= 20, font=("Peroetua", 10 ), bg='#E0CCBE')
        self.result_entry.place (x = 120, y = 8)
        
        self.evaluation_result_label = None
        
        self.height_cm_entry.bind('<KeyRelease>', self.update_height_cm)
        self.height_m_entry.bind('<KeyRelease>', self.update_height_m)

        #Logout
    #     self.Logout_Page = tk.Button (self.main_frame, text = 'Return', cursor='gumby', bg="grey", fg="white", font=("SimSun"), relief="raised", height=1, width=15, command=self.go_to_logout_page)
    #     self.Logout_Page.place(x=5, y=5)
        
    # def go_to_logout_page(self):
    #     self.master.change_window('Logout') 
    
  
    def update_weight_lb(self, event):
        try:
            kg_value = float(self.weight_kg_entry.get())
            lb_value = kg_value * 2.20462
            self.weight_lb_entry.delete(0, tk.END)
            self.weight_lb_entry.insert(0, f"{lb_value:.2f}")
        except ValueError:
            self.weight_lb_entry.delete(0, tk.END)
            self.weight_lb_entry.insert(0, "Invalid Input")

    def update_weight_kg(self, event):
        try:
            lb_value = float(self.weight_lb_entry.get())
            kg_value = lb_value / 2.20462
            self.weight_kg_entry.delete(0, tk.END)
            self.weight_kg_entry.insert(0, f"{kg_value:.2f}")
        except ValueError:
            self.weight_kg_entry.delete(0, tk.END)
            self.weight_kg_entry.insert(0, "Invalid Input")

    def update_height_cm(self, event):
        try:
            cm_value = float(self.height_cm_entry.get())
            m_value = cm_value / 100
            self.height_m_entry.delete(0, tk.END)
            self.height_m_entry.insert(0, f"{m_value:.2f}")
        except ValueError:
            self.height_m_entry.delete(0, tk.END)
            self.height_m_entry.insert(0, "Invalid Input")

    def update_height_m(self, event):
        try:
            m_value = float(self.height_m_entry.get())
            cm_value = m_value * 100
            self.height_cm_entry.delete(0, tk.END)
            self.height_cm_entry.insert(0, f"{cm_value:.2f}")
        except ValueError:
            self.height_cm_entry.delete(0, tk.END)
            self.height_cm_entry.insert(0, "Invalid Input")
    
    def clear_button(self):
        self.height_cm_entry.delete(0, tk.END)
        self.height_m_entry.delete(0, tk.END)
        self.weight_kg_entry.delete(0, tk.END)
        self.weight_lb_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        
        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()
            self.evaluation_result_label = None
            
    def calculate_BMI(self):
        try:
            kg_value = float(self.weight_kg_entry.get())
            m_value = float(self.height_m_entry.get())
            bmi_result = kg_value / (m_value ** 2)  
            self.result_entry.delete(0, tk.END)  
            self.result_entry.insert(0, f"{bmi_result:.2f}")
            
            self.Evaluation_result(bmi_result)
            
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Invalid Input")
            
            
    def Evaluation_result(self, bmi_result):
        if bmi_result < 18.5:
            category = 'Underweight'
        elif bmi_result <= 24.9:
            category = 'Healthy'
        elif bmi_result <= 29.9:
            category = 'Overweight'
        elif bmi_result <= 34.9:
            category = 'Obese'
        else:
            category = 'Extremely Obese'

        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()

        self.evaluation_result_label = tk.Label(self.main_frame, text=f'You are {category}', foreground='grey', font=("Poor Richard", 19, 'bold'))
        self.evaluation_result_label.place(x=50, y=500)
        

    def go_to_welcome_page(self):
        choice = messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?")
        if choice:
            self.master.change_window('Welcome_Page')
        else:
            pass

    def got_to_profile_page(self):
        self.parent.change_window('Profile')
        
    def save_info(self):
        user_id = self.parent.frames['Signup'].user_id
        age = self.age_entry.get().strip()
        kg = self.weight_kg_entry.get().strip()
        lb = self.weight_lb_entry.get().strip()
        cm = self.height_cm_entry.get().strip()
        m = self.height_m_entry.get().strip()

        save = Save_info()  # Corrected instantiation
        save.age = age
        save.kilogram = kg
        save.pounds = lb
        save.centimeter = cm
        save.meter = m

        dbconn = Database()  # Corrected class instantiation
        dbconn.create_save_info_table(save, user_id)
        dbconn.conn.close()

    def history_info(self):
        pass
        
    def on_return(self):
        pass
            
class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.login_bg = tk.Frame(self, bg='#3C3633', height=400, width=350)
        self.login_bg.place(x=0, y=0)

        self.welcome1_label = tk.Label(self, text="WELCOME TO", font="Arial 25 bold", bg='#3C3633', foreground='#faf1e8')
        self.welcome1_label.place(x=57, y=40)
        self.welcome2_label = tk.Label(self, text="BMI CALCULATOR", font="Arial 25 bold", bg='#3C3633', foreground='#faf1e8')
        self.welcome2_label.place(x=20, y=80)

        # Define font style
        font_style = ("Garamond", 15, "bold")

        self.login_btn = CTkButton(self, text="Login", height=50, width=50, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.go_to_login_page)
        self.login_btn.place(x=130, y=185)

        self.sign_up_btn = CTkButton(self, text="Signup", bg_color='#3C3633', height=50, width=50, hover_color="#747264", fg_color='#B09079', 
                                     font=font_style, corner_radius=30, text_color='black',command=self.go_to_Sign_up_Page)
        self.sign_up_btn.place(x=125, y=270)
        
    def go_to_Sign_up_Page(self):
        self.parent.frames['Signup'].Bday_calendar_entry.delete(0, tk.END)
        self.parent.change_window('Signup')

    def go_to_login_page(self):
        self.parent.change_window('Login')
        
    def on_return(self):
        pass


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")
        self.frames = {}
        self.frames['Welcome_Page'] = Welcome(self)  # Assuming you have a Welcome frame
        self.frames['Login'] = Login(self)
        self.frames['Signup'] = Signup(self)
        self.frames['Photo'] = Photo(self, self.frames['Signup'])
        self.frames['BMI'] = BMI(self)
        self.change_window('Welcome_Page')  # Change to the Welcome_Page initially

    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        self.frames[name].grid()


root = MainWindow()
root.resizable(False, False)
root.mainloop()

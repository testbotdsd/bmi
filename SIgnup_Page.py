import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
import Model
import Data_base_Handler
import random
import string
import os
from captcha.image import ImageCaptcha
import random
from tkcalendar import DateEntry
from datetime import date

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
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
    
class Photo(tk.Frame):
    def __init__(self, master, signup_frame):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.signup_frame = signup_frame
        self.config(width=400, height=600)
        
        self.Photo_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.Photo_bg.place(x=0, y=0)
        
        img=self.generate_captha()
        self.pic_frame = tk.Label(self, image=img)
        self.pic_frame.image = img  
        self.pic_frame.place(x=125, y=70)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = tk.Button(self, text='Sign Up', width=21, font=('Courier', 15, 'bold'), bg='#d3d3d3', command=self.go_to_Login_Page)
        self.Finish_button.place(x=65, y=517)
        
        self.captcha_label = tk.Label(self, text='Captcha', font=('Courier', 12, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.captcha_label.place(x=160, y=255)

        self.generate_captcha_button = tk.Button(self, text="Generate Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3', command=self.generate_captcha)
        self.generate_captcha_button.place(x=110, y=290)

        self.check_var = tk.IntVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable= self.check_var, 
                                                                command=self.terms_conditios_var)
        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self.Photo_bg, text="I accept the Terms and Conditions", variable=self.terms_and_conditions_var, bg='#3C3633', fg="white")
        self.terms_and_conditions_check_button.place(x=95, y=484)

    def generate_captcha(self):
        print("Reload button clickd")
        img = self.generate_captha()
        self.pic_frame.configure(image=img)
        self.pic_frame.image = img


    def generate_captha(self):
        self.generated = "".join(random.choices(string.ascii_lowercase, k=4))
        captcha = ImageCaptcha(width=300, height=200)
        captcha_text = f'{self.generated}'
        img_data = captcha.generate(captcha_text)
        img = tk.PhotoImage(data=img_data.getvalue())
        
        
        return img
    
   

    def terms_conditios_var(self):
            result = messagebox.askokcancel("Terms and condition", "Do you accept the Terms and Conditions?")
            if result:
                self.check_var.set(1)
            else:
                self.check_var.set(0)

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

        user = Model.User()
        user.firstname = FName
        user.lastname = LName
        user.username = Uname
        user.birthday = Bday
        user.gmail = Gmail
        user.password = Pass
        
        if Pass == Confirm_Pass:
            
            dbconn = Data_base_Handler.database()
            dbconn.create_sign_up_table(user)
            dbconn.conn.close()
            
        else:
            messagebox.showerror("Error", "Incorrect Password.")
            return
        
        final = messagebox.askokcancel('Signup', 'Finish signing up?')
        if final:
            self.parent.frames['Signup'].clear_input()
            self.parent.change_window('Login')


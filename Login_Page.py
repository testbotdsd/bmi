import tkinter as tk
from tkinter import messagebox
from customtkinter import *
import random
import string
import SIgnup_Page
import Data_base_Handler
from captcha.image import ImageCaptcha

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=450, height=600)
    
        self.login_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self.login_bg, text="WELCOME", font=('Courier', 45, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.welcome_label.place(x=95, y=30)

        self.username_label = tk.Label(self.login_bg, text="Username", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=81, y=104)

        self.username_entry = tk.Entry(self.login_bg, border=1, width=23, font=('Courier', 15),fg='white', bg='#59504b')
        self.username_entry.place(x=81, y=138)

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.pass_label.place(x=81, y=191)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=19, font=('Courier', 15), fg='white', bg='#59504b', show='*')
        self.pass_entry.place(x=81, y=225)

        self.toggle_password_button = tk.Button(self.login_bg, text="Show", font=('Courier', 10), bd=1, bg='white',fg='black', command=self.toggle_password)
        self.toggle_password_button.place(x=322, y=225)


        self.forgot_password_button = tk.Button(self.login_bg, text='Forgot your password?',  font=('Courier', 11), fg='#5e918e', 
                                                bg='#3C3633', bd=0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=166, y=263)

        self.login_button = CTkButton(self.login_bg, text='LOGIN', width=300,height=40,corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', 
                                        text_color='black',command=self.validate_login)
        self.login_button.place(x=81, y=510)

        self.no_account_label = tk.Label(self.login_bg, text="Don't have an account?", bg='#3C3633', font="Courier 10", foreground='#EEEDEB')
        self.no_account_label.place(x=82, y=558)

        self.sign_up_btn = tk.Button(self.login_bg, text="Sign up now", bg='#3C3633', bd=0, font=('Courier', 10, 'bold'), 
                                        command=self.go_to_signup, foreground='#5e918e')
        self.sign_up_btn.place(x=264, y=557)

        self.password_hidden = True 

        self.check_var = tk.IntVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable=self.check_var, 
                                                                command=self.terms_conditions_var)
        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button.place(x=95, y=484)
        
        self.captcha_label = tk.Label(self.login_bg, text='Captcha', font=('Courier', 30, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.captcha_label.place(x=140, y=305)

        self.generate_captcha_button = tk.Button(self.login_bg, text="Generate Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3', 
                                                 command=self.generate_captcha)
        self.generate_captcha_button.place(x=235, y=375)

        # self.captcha_entry = CTkEntry(self)
        self.captcha_entry = tk.Entry(self.login_bg, border=1, width=12, font=('Courier', 15), fg='white', bg='#59504b')
        self.captcha_entry.place(x=70, y=375)

        self.captcha_window = None
        self.captcha_label_in_window = None

    def generate_captcha(self):
        if not self.captcha_window:
            self.captcha_window = tk.Toplevel(self.parent)
            self.captcha_window.title("Captcha")
        
        img = self.generate_captcha_image()
        
        if self.captcha_label_in_window:
            self.captcha_label_in_window.config(image=img)
            self.captcha_label_in_window.image = img
        else:
            self.captcha_label_in_window = tk.Label(self.captcha_window, image=img)
            self.captcha_label_in_window.image = img
            self.captcha_label_in_window.pack()

    def generate_captcha_image(self):
        generated = "".join(random.choices(string.ascii_lowercase, k=6))
        captcha = ImageCaptcha(width=300, height=200)
        captcha_text = f'{generated}'
        img_data = captcha.generate(captcha_text)
        img = tk.PhotoImage(data=img_data.getvalue())
        return img

    def terms_conditions_var(self):
        result = messagebox.askokcancel("Terms and condition", "Do you accept the Terms and Conditions?")
        if result:
            self.check_var.set(1)
        else:
            self.check_var.set(0)

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

        dbconn = Data_base_Handler.database()
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
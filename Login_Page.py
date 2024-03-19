import tkinter as tk
from tkinter import messagebox
from customtkinter import *

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
        self.parent.change_window('Forgot_Password')

    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')
    
    def go_to_signup(self):
        self.parent.change_window('Signup')

    def validate_login(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()
        
        if username == "" or password == "":
            messagebox.showerror("Error", "Please fill in both username and password fields.")
        else:
            self.reset_fields()
            self.go_to_BMI_Page()

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)

class Forgot_Password (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.current_step = 1
        
        self.email_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.email_label_bg.place(x=0, y=0)
        
        self.forgot_label = tk.Label(self.email_label_bg, text="Forgot Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.forgot_label.place(x=100, y=50)
        
        self.email_label = tk.Label(self.email_label_bg, text="Email", font=('Courier', 15), fg='white', bg='#3C3633')
        self.email_label.place(x=100, y=110)

        self.email_entry = tk.Entry(self.email_label_bg, font=('Courier', 12), bg='#59504b')
        self.email_entry.place(x=100, y=145)
        
        self.continue_btn_email = CTkButton(self.email_label_bg, text="Continue", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.continue_clicked)
        self.continue_btn_email.place(x=100, y=490)

        self.verification_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)

        self.verification_code_label = tk.Label(self.verification_label_bg, text="Enter Verification Code", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_code_label.place(x=100, y=110)

        self.verification_code_entry = tk.Entry(self.verification_label_bg, font=('Courier', 12), bg='#59504b')
        self.verification_code_entry.place(x=100, y=145)

        self.return_btn_2 = tk.Button(self.verification_label_bg, text="Return", font=('Courier', 12), bg='#59504b', command=lambda: self.return_to_step(1))
        self.return_btn_2.place(x=10, y=10)

        self.continue_btn_verification = CTkButton(self.verification_label_bg, text="Continue", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.continue_clicked)
        self.continue_btn_verification.place(x=100, y=490)
        

        self.reset_password_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        
        self.new_password_label = tk.Label(self.reset_password_label_bg, text="New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.new_password_label.place(x=100, y=110)

        self.new_password_entry = tk.Entry(self.reset_password_label_bg, font=('Courier', 12), show='*', bg='#59504b')
        self.new_password_entry.place(x=100, y=145)

        self.confirm_password_label = tk.Label(self.reset_password_label_bg, text="Confirm Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.confirm_password_label.place(x=100, y=190)

        self.confirm_password_entry = tk.Entry(self.reset_password_label_bg, font=('Courier', 12), show='*', bg='#59504b')
        self.confirm_password_entry.place(x=100, y=225)

        self.return_btn_3 = tk.Button(self.reset_password_label_bg, text="Return", font=('Courier', 12), bg='#59504b', command=lambda: self.return_to_step(2))
        self.return_btn_3.place(x=10, y=10)

        self.reset_btn = CTkButton(self.reset_password_label_bg, text="Reset Password", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.continue_clicked)
        self.reset_btn.place(x=100, y=490)

        self.show_step(1)

    def show_step(self, step):
        if step == 1:
            self.email_label_bg.place(x=0, y=0)
            if hasattr(self, 'verification_label_bg'):
                self.verification_label_bg.place_forget()
            if hasattr(self, 'reset_password_label_bg'):
                self.reset_password_label_bg.place_forget()
        elif step == 2:
            if hasattr(self, 'email_label_bg'):
                self.email_label_bg.place_forget()
            self.verification_label_bg.place(x=0, y=0)
            if hasattr(self, 'reset_password_label_bg'):
                self.reset_password_label_bg.place_forget()
        elif step == 3:
            if hasattr(self, 'email_label_bg'):
                self.email_label_bg.place_forget()
            if hasattr(self, 'verification_label_bg'):
                self.verification_label_bg.place_forget()
            self.reset_password_label_bg.place(x=0, y=0)
            
    

    def return_to_step(self, step):
        self.current_step = step
        self.show_step(self.current_step)

    def continue_clicked(self):
        if self.current_step == 1:
            self.current_step = 2
            self.show_step(self.current_step)
        elif self.current_step == 2:
            self.current_step = 3
            self.show_step(self.current_step)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="Return", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

    def go_to_login(self):
        self.parent.change_window('Login')
    
    def on_return(self):
        pass

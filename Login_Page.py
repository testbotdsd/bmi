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
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.forgot_password_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.forgot_password_label_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.forgot_password_label_bg, text="Forgot Password", font=('Courier', 20, 'bold'), fg='white', bg='#3C3633')
        self.forgot_password_label.place(x = 80, y = 40)

        # gmail num
        self.gmail_num_label = tk.Label(self.forgot_password_label_bg, text="Gmail Account", font=('Courier', 15), fg='white', bg='#3C3633')
        self.gmail_num_label.place(x = 100, y= 110)
        
        self.gmail_num_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12),bg='#59504b')
        self.gmail_num_entry.place(x= 100, y= 145)

        #new pass
        self.new_password_label = tk.Label(self.forgot_password_label_bg, text="New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.new_password_label.place( x = 100, y= 190)
        
        self.new_password_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), show='*', bg='#59504b')
        self.new_password_entry.place(x = 100, y= 225)

        #conf pass
        self.confirm_password_label = tk.Label(self.forgot_password_label_bg, text="Confirm Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.confirm_password_label.place(x= 100, y= 270)
        
        self.confirm_password_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), show='*,' , bg='#59504b')
        self.confirm_password_entry.place(x = 100, y = 305)
        
        #verification
        self.verification_label = tk.Label(self.forgot_password_label_bg, text="Verification", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label.place(x= 100, y= 350)
        
        self.verification_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), bg='#59504b')
        self.verification_entry.place(x = 100, y = 385)

        #cont button
        self.continue_button = CTkButton(self, text='Continue', width=200, height=40,corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', 
                                            text_color='black', command=self.go_to_login)
        self.continue_button.place( x =100, y = 490)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

    def go_to_login(self):
        self.parent.change_window('Login')
    
    def on_return(self):
        pass

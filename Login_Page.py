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
        self.parent.change_window('Forgot_Password_Gmail')

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

class Forgot_Password_Gmail (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.forgot_password_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.forgot_password_label_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.forgot_password_label_bg, text="Forgot Password", font=('Courier', 20, 'bold'), fg='white', bg='#3C3633')
        self.forgot_password_label.place(x = 70, y = 40)

        # gmail
        self.gmail_label = tk.Label(self.forgot_password_label_bg, text="GMAIL", font=('Courier', 15), fg='white', bg='#3C3633')
        self.gmail_label.place(x = 100, y= 110)
        
        self.gmail_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), fg='white', bg='#59504b')
        self.gmail_entry.place(x= 100, y= 145)

        #cont button
        self.continue_button = CTkButton(self.forgot_password_label_bg, text="CONTINUE", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.validate_gmail_entry)
        self.continue_button.place( x =100, y = 440)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', 
                                     command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

    def go_to_otp(self):
        self.parent.change_window('OTP')

    def go_to_login(self):
        self.parent.change_window('Login')   

    def validate_gmail_entry(self):
        gmail = self.gmail_entry.get()
        
        if gmail == "":
            messagebox.showerror("Error", "Please enter your Gmail Account.")
        else:
            self.reset_fields()
            self.go_to_otp()

    def reset_fields(self):
        self.gmail_entry.delete(0, tk.END)
    
class OTP (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.forgot_password_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.forgot_password_label_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.forgot_password_label_bg, text="OTP", font=('Courier', 20, 'bold'), fg='white', bg='#3C3633')
        self.forgot_password_label.place(x = 170, y = 40)

        # verification
        self.verification_label = tk.Label(self.forgot_password_label_bg, text="Enter Verification Code", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label.place(x = 70, y= 110)
        
        self.verification_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), fg='white', bg='#59504b')
        self.verification_entry.place(x= 100, y= 145)

        #cont button
        self.continue_button = CTkButton(self.forgot_password_label_bg, text="Continue", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.validate_otp_entry)
        self.continue_button.place( x =100, y = 440)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', 
                                     command=self.go_to_forget_pass)
        self.back_button.place(x= 5, y= 10)

    def go_to_forget_pass(self):
        self.parent.change_window('Forgot_Password_Gmail')

    def go_to_reset_pass(self):
        self.parent.change_window('Reset_Pass') 

    def validate_otp_entry(self):
        otp_entry = self.verification_entry.get()
        
        if otp_entry == "":
            messagebox.showerror("Error", "Please enter the OTP that was sent on your GMAIL Account.")
        else:
            self.reset_fields()
            self.go_to_reset_pass()

    def reset_fields(self):
        self.verification_entry.delete(0, tk.END)

class Reset_Pass (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.forgot_password_label_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.forgot_password_label_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.forgot_password_label_bg, text="Reset Password", font=('Courier', 20, 'bold'), fg='white', bg='#3C3633')
        self.forgot_password_label.place(x = 90, y = 30)

        # New Password
        self.verification_label = tk.Label(self.forgot_password_label_bg, text="Enter New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label.place(x = 90, y= 130)
        
        self.verification_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), fg='white', bg='#59504b', show='*')
        self.verification_entry.place(x= 100, y= 165)

        self.toggle_password_button = tk.Button(self, text="Show", font=('Courier', 10), bd=1, bg='white',fg='black', command=self.toggle_password)
        self.toggle_password_button.place(x=180, y=230)

        # Confirm Password
        self.verification_label_2 = tk.Label(self.forgot_password_label_bg, text="Confirm New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label_2.place(x = 85, y= 290)
        
        self.verification_entry_2 = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), fg='white', bg='#59504b', show='*')
        self.verification_entry_2.place(x= 100, y= 325)

        #cont button
        self.continue_button = CTkButton(self.forgot_password_label_bg, text="Continue", width=200, height=40, corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',command=self.validate_password_and_confirm_password_entry)
        self.continue_button.place( x =100, y = 440)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', 
                                     command=self.go_to_otp)
        self.back_button.place(x= 5, y= 10)

        self.password_hidden = True

    def validate_password_and_confirm_password_entry(self):
        passsword_and_confirm_password = self.verification_entry and self.verification_entry_2.get()
        
        if passsword_and_confirm_password == "":
            messagebox.showerror("Error", "Please enter your New Password and Confirm New Password.")
        else:
            self.reset_fields()
            self.reset_fields_2()
            self.go_to_login()

    def toggle_password(self):
        if self.password_hidden:
            self.verification_entry.config(show='')
            self.verification_entry_2.config(show='')
            self.toggle_password_button.config(text="Hide", bg='#3C3633', fg='white')
            self.password_hidden = False
        else:
            self.verification_entry.config(show='*')
            self.verification_entry_2.config(show='*')
            self.toggle_password_button.config(text="Show", bg='white', fg='#3C3633')
            self.password_hidden = True

    def reset_fields(self):
        self.verification_entry.delete(0, tk.END)

    def reset_fields_2(self):
        self.verification_entry_2.delete(0, tk.END)

    def go_to_otp(self):
        self.parent.change_window('OTP')

    def go_to_login(self):
        self.parent.change_window('Login')  
    
    def on_return(self):
        pass
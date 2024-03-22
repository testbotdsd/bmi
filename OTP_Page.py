import tkinter as tk
from tkinter import messagebox
from customtkinter import *
import random
import smtplib
import re
import Login_Page
import Data_base_Handler
import Model

class Forget(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.frame_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.frame_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.frame_bg, text="Forgot Password", font=('Courier', 20, 'bold'), fg='white', 
                                              bg='#3C3633')
        self.forgot_password_label.place(x = 70, y = 40)

        # gmail
        self.gmail_label = tk.Label(self.frame_bg, text="GMAIL", font=('Courier', 15), fg='white', bg='#3C3633')
        self.gmail_label.place(x = 100, y= 110)
        
        self.gmail_entry = tk.Entry(self.frame_bg, font=('Courier', 12), fg='white', bg='#59504b')
        self.gmail_entry.place(x= 100, y= 145)

        #send otp button
        self.send_otp_button = CTkButton(self.frame_bg, text="Send OTP", width=200, height=40, corner_radius=30, 
                                         font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',
                                         command=self.validate_login)
        self.send_otp_button.place(x=100, y=193)

        #otp
        self.verification_label = tk.Label(self.frame_bg, text="Enter Verification Code", font=('Courier', 15), fg='white', 
                                           bg='#3C3633')
        self.verification_label.place(x=70, y=261)

        self.otp_verify_entry = tk.Entry(self.frame_bg, font=('Courier', 12), fg='white', bg='#59504b')
        self.otp_verify_entry.place(x=100, y=296)

        self.continue_button = CTkButton(self.frame_bg, text="Continue", width=200, height=40, corner_radius=30, 
                                         font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', text_color='black',
                                         command=self.verify_otp)
        self.continue_button.place(x=100, y=440)

        #back button
        self.back_button = tk.Button(self.frame_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', 
                                     command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

    def check_gmail(self, gmail):
        data = Data_base_Handler.database()
        return data.checking_gmail_exist(gmail)
    
    def validate_login(self):
        gmail = self.gmail_entry.get()
        otp = self.otp_verify_entry.get()
        
        if not self.check_gmail(gmail):
            messagebox.showerror("Error", "Gmail does not exist. Please enter the gmail you used during sign up.")
            return

        if gmail == "":
            messagebox.showerror("Error", "Please enter your Gmail Account.")
            return None
        
        if not self.is_valid_gmail(gmail):
            messagebox.showerror("Error", "Please enter a valid Gmail Account.")
            return None
        
        # Generate a 4-digit OTP
        self.otp = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        
        email_sender = 'gelcabsam@gmail.com'
        password = 'wnet spkm cjak ofiw'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        msg = 'Subject: Your OTP\n\nHello, your OTP is ' + self.otp
        server.sendmail(email_sender, gmail, msg)
        server.quit()

        # Set OTP and email for OTP frame
        otp_frame = self.parent.frames['Reset_Password']
        otp_frame.sent_otp = self.otp
        otp_frame.email = gmail
        
        self.reset_fields()

    def verify_otp(self):
        entered_otp = self.otp_verify_entry.get()
        
        if entered_otp == "":
            messagebox.showerror("Error", "Please enter the OTP.")
            return
        
        if entered_otp == self.otp:
            # Correct OTP entered
            messagebox.showinfo("Success", "OTP verified. You can now reset your password.")
            self.go_to_reset_pass()
            self.parent.change_window('Reset_Password')
        else:
            # Incorrect OTP entered
            messagebox.showerror("Error", "Incorrect OTP. Please try again.")

    
    def reset_fields(self):
        self.gmail_entry.delete(0, tk.END)

    def is_valid_gmail(self, email):
        # Check if the email follows a valid format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        
        # Check if the domain is gmail.com
        if email.endswith('@gmail.com'):
            return True
        
        return False

    def go_to_otp(self):
        self.parent.change_window('OTP')

    def go_to_login(self):
        self.parent.change_window('Login')

    def go_to_reset_pass(self):
        self.parent.change_window('Reset_Password') 

    def reset_fields(self):
        self.otp_verify_entry.delete(0, tk.END)

    def on_return(self, **kwargs):
        pass



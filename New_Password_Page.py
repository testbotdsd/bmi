import tkinter as tk
from tkinter import messagebox
from customtkinter import *

class Reset_Password (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.frame_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.frame_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.frame_bg, text="Reset Password", font=('Courier', 20, 'bold'), fg='white', bg='#3C3633')
        self.forgot_password_label.place(x = 90, y = 30)

        # New Password
        self.verification_label = tk.Label(self.frame_bg, text="Enter New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label.place(x = 90, y= 130)
        
        self.verification_entry = tk.Entry(self.frame_bg, font=('Courier', 12), fg='white', bg='#59504b', show='*')
        self.verification_entry.place(x= 100, y= 165)

        self.toggle_password_button = tk.Button(self, text="Show", font=('Courier', 10), bd=1, bg='white',fg='black', command=self.toggle_password)
        self.toggle_password_button.place(x=180, y=230)

        # Confirm Password
        self.verification_label_2 = tk.Label(self.frame_bg, text="Confirm New Password", font=('Courier', 15), fg='white', bg='#3C3633')
        self.verification_label_2.place(x = 85, y= 290)
        
        self.verification_entry_2 = tk.Entry(self.frame_bg, font=('Courier', 12), fg='white', bg='#59504b', show='*')
        self.verification_entry_2.place(x= 100, y= 325)

        #cont button
        self.continue_button = CTkButton(self.frame_bg, text="Continue", width=200, height=40, 
                                         corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', 
                                         fg_color='#E0CCBE', text_color='black',
                                         command=self.validate_entries)
        self.continue_button.place( x =100, y = 440)

        #back button
        self.back_button = tk.Button(self.frame_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', 
                                     command=self.go_to_otp)
        self.back_button.place(x= 5, y= 10)

        self.password_hidden = True

    def validate_entries(self):
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
        self.parent.change_window('Forget')

    def go_to_login(self):
        self.parent.change_window('Login') 

    def on_return(self, **kwargs):
        pass
        
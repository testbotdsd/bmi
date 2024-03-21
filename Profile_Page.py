import tkinter as tk
from customtkinter import *
from tkinter import messagebox

class Profile(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        self.profile_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.profile_bg.place(x=0, y=0)

        font_style = ("Garamond", 15, "bold")

        self.profile_label = tk.Label(self, text="PROFILE", bg='#3C3633', font=('Courier', 30, 'bold'), 
                                        foreground='#E0CCBE')
        self.profile_label.place(x=115, y=10)

        self.pic_frame = tk.Frame(self, bd=10, width=150, height=150, bg='#747264', relief='flat')
        self.pic_frame.place(x=45, y=70)

        self.name_label = tk.Label(self, text="Name:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.name_label.place(x=40, y=240)

        self.birthday_label = tk.Label(self, text="Birthday:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=40, y=300)

        self.gmail_label = tk.Label(self, text="Gmail:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.gmail_label.place(x=40, y=360)

        self.username_label = tk.Label(self, text="Username:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=40, y=420)

        self.logout_btn = CTkButton(self, text="Logout", height=50, width=50, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.go_to_start)
        self.logout_btn.place(x=151, y=530)
        
        self.return_btn = CTkButton(self, text="Return", height=50, width=50, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.go_to_BMI_page)
        self.return_btn.place(x=5, y=5)
        
    def go_to_start(self):
        logout = messagebox.askyesno("BMI Logout", "Are you sure you want to logout?")
        if logout == True:
            self.parent.change_window('Welcome_Page')
        else:
            return False
        
    def go_to_BMI_page(self):
        self.parent.change_window('BMI')

    def on_return(self):
        pass
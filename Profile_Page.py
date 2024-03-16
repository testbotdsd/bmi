import tkinter as tk
from customtkinter import *

class Profile(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        self.profile_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.profile_bg.place(x=0, y=0)

        font_style = ("Garamond", 15, "bold")

        self.profile_label = tk.Label(self, text="PROFILE", bg='#3C3633', font=('Courier', 17, 'bold'), 
                                        foreground='#E0CCBE')
        self.profile_label.place(x=140, y=10)

        self.pic_frame = tk.Frame(self, bd=10, width=100, height=100, bg='#747264', relief='flat')
        self.pic_frame.place(x=45, y=70)

        self.name_label = tk.Label(self, text="Name:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.name_label.place(x=40, y=206)

        self.birthday_label = tk.Label(self, text="Birthday:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=40, y=252)

        self.information_label = tk.Label(self, text="Information:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.information_label.place(x=40, y=298)

        self.logout_btn = CTkButton(self, text="Logout", height=50, width=50, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.go_to_main_page)
        self.logout_btn.place(x=151, y=530)
        
    def go_to_main_page(self):
        self.parent.change_window('Welcome_Page')

    def on_return(self):
        pass

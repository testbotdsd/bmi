import tkinter as tk
from customtkinter import *

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

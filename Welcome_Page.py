import tkinter as tk
from customtkinter import *

class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=350, height=400)
        # self.customtkinter = CustomTkinter()
        # self.customtkinter.set_default_color_theme("dark")
        # self.customtkinter.set_appearance_mode("dark")

        self.login_bg = tk.Frame(self, bg='#3C3633', height=400, width=350)
        self.login_bg.place(x=0, y=0)

        self.welcome1_label = tk.Label(self, text="WELCOME TO", font="Arial 25 bold", bg='#3C3633', foreground='#faf1e8')
        self.welcome1_label.place(x=57, y=40)
        self.welcome2_label = tk.Label(self, text="BMI CALCULATOR", font="Arial 25 bold", bg='#3C3633', foreground='#faf1e8')
        self.welcome2_label.place(x=20, y=80)

<<<<<<< HEAD
        # Define font style
        font_style = ("Garamond", 15, "bold")

        self.login_btn = CTkButton(self, text="Login", height=50, width=50, bg_color="#7B6079", font=font_style, fg_color="#DE8971", hover_color='Blue', corner_radius=30, command=self.go_to_login_page)
        self.login_btn.place(x=130, y=185)

        self.sign_up_btn = CTkButton(self, text="Signup", bg_color='#7B6079', height=50, width=50, hover_color="pink", fg_color='#DE8971', font=font_style, corner_radius=30, command=self.go_to_Sign_up_Page)
        self.sign_up_btn.place(x=125, y=270)
        
        # self.dark_light_btn = CTkButton(self, text='light/dark mode', command=self.change)
        # self.dark_light_btn.place(x=1, y=1)
        
    #     self.mode = "dark"

    # def change(self):
    #     if self.mode == "dark":
    #         self.customtkinter.set_appearance_mode("light")
    #         self.mode = "light"
    #     else:
    #         self.customtkinter.set_appearance_mode("dark")
    #         self.mode = "dark"
=======
        self.login_btn = tk.Button(self, text="Login", font="Garamond 15 bold", width=13, bg="#E0CCBE", command=self.go_to_login_page)
        self.login_btn.place(x=95, y=185)

        self.sign_up_btn = tk.Button(self, text="Signup", font="Garamond 15 bold", width=13, bg="#B09079", command=self.go_to_Sign_up_Page)
        self.sign_up_btn.place(x=95, y=245)
>>>>>>> a349df16829c39a4dddba2b93c5d214be48ac51a
        
    def go_to_Sign_up_Page(self):
        self.parent.change_window('Signup')

    def go_to_login_page(self):
        self.parent.change_window('Login')
        
    def on_return(self):
        pass

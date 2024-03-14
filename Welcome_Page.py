import tkinter as tk

class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.login_bg = tk.Frame(self, bg='#4F4A45', height=400, width=350)
        self.login_bg.place(x=0, y=0)

        self.welcome1_label = tk.Label(self, text="WELCOME TO", font="Arial 25 bold", bg='#4F4A45', foreground='#ED7D31')
        self.welcome1_label.place(x=57, y=40)
        self.welcome2_label = tk.Label(self, text="BMI CALCULATOR", font="Arial 25 bold", bg='#4F4A45', foreground='#ED7D31')
        self.welcome2_label.place(x=20, y=80)

        self.login_btn = tk.Button(self, text="Login", font="Garamond 12 bold", width=12, command=self.go_to_login_page)
        self.login_btn.place(x=120, y=195)

<<<<<<< HEAD
        self.sign_up_btn = tk.Button(self, text="Signup", font="Garamond 12 bold", width=12, command=self.go_to_Sign_up_Page)
        self.sign_up_btn.place(x=100, y=235)
=======
        self.sign_up_btn = tk.Button(self, text="Signup", font="Garamond 12 bold", width=12)
        self.sign_up_btn.place(x=120, y=235)
>>>>>>> f09cd3ff4894026e9b3755b5436b99ec489effc9
        
    def go_to_Sign_up_Page(self):
        self.master.change_window('Signup')

    def go_to_login_page(self):
        self.master.change_window('Login')
        
    def on_return(self):
        pass

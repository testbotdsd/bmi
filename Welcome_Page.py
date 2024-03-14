import tkinter as tk

class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.login_bg = tk.Frame(self, bg='#7B6079', height=400, width=350)
        self.login_bg.place(x=0, y=0)

        self.welcome1_label = tk.Label(self, text="WELCOME TO", font="Arial 25 bold", bg='#7B6079', foreground='#faf1e8')
        self.welcome1_label.place(x=57, y=40)
        self.welcome2_label = tk.Label(self, text="BMI CALCULATOR", font="Arial 25 bold", bg='#7B6079', foreground='#faf1e8')
        self.welcome2_label.place(x=20, y=80)

        self.login_btn = tk.Button(self, text="Login", font="Garamond 15 bold", width=13, bg="#DE8971", command=self.go_to_login_page)
        self.login_btn.place(x=95, y=185)

        self.sign_up_btn = tk.Button(self, text="Signup", font="Garamond 15 bold", width=13, bg="#f7d4cb", command=self.go_to_Sign_up_Page)
        self.sign_up_btn.place(x=95, y=245)
        
    def go_to_Sign_up_Page(self):
        self.master.change_window('Signup')

    def go_to_login_page(self):
        self.master.change_window('Login')
        


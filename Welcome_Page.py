import tkinter as tk

class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.start_label = tk.Label (self, text="BMI CALCULATOR", bg="grey", font="Algeria 25")
        self.start_label.place(x=40, y=10)
        
        self.login_label = tk.Button(self, text="Login", bg="grey", width=30, command=self.go_to_login_page)
        self.login_label.place(x=100, y=300)
        
        self.signup_label = tk.Button(self, text="Sign Up", bg="grey", width=30)
        self.signup_label.place(x=100, y=400)
        

    def go_to_login_page(self):
        self.master.change_window('Login')
        
    def on_return(self):
        pass

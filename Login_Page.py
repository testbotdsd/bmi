import tkinter as tk

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        self.back_button = tk.Button(self, text="back", command=self.go_to_login)
        self.back_button.place(x=30, y=30)

        self.Login_button = tk.Frame(self, text="Login")
        self.Login_button.place (x=70, y=30)
        
    def go_to_BMI_Page(self):
        self.parent.change_window('BMI_Page')

    def go_to_login(self):
        self.parent.change_window('Front_Page')

    def on_return(self):
        pass

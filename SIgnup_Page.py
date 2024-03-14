import tkinter as tk

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.back_button = tk.Button(self, text="back", command=self.go_to_welcome_page)
        self.back_button.place(x=30, y=30)

        self.continue_button = tk.Button(self, text='Login', command=self.go_to_Login_Page)
        self.continue_button.place(x=70, y=30)


    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')


    def go_to_Login_Page(self):
        self.parent.change_window('Login')


    def on_return(self):
        pass
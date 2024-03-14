import tkinter as tk

class Login (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
    
        #ANGELAINE NEW
        self.welcome_label = tk.Label(self, text="WELCOME", font="Arial 20 bold")
        self.welcome_label.place(x=0, y=0)

        self.email_entry = tk.Entry(self, border=1)
        self.email_entry.place(x=10, y=50)

        self.back_button = tk.Button(self, text="back", command=self.go_to_welcome_page)
        self.back_button.place(x=30, y=550)

        self.continue_button = tk.Button(self, text='Login', command=self.go_to_BMI_Page)
        self.continue_button.place(x=70, y=550)

        self.forgot_password_button = tk.Button(self, text = 'Forgot your password?', bd = 0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x= 30, y=50)

    def go_to_forgot_password(self):
        self.parent.change_window('Forgot_Password')

    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')

    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')

class Forgot_Password (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.forgot_label = tk.Label (self, text='forgot password', font='arial 20')
        self.forgot_label.place (x=10, y=30)

        self.back_button = tk.Button(self, text='back', command=self.go_to_login)
        self.back_button.place(x=10, y=50)

    def go_to_login(self):
        self.parent.change_window('Login')
    

    def on_return(self):
        pass

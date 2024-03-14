import tkinter as tk

class Login (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
    
        #ANGELAINE NEW
        self.login_bg = tk.Frame(self, bg='#4F4A45', height=600, width=400)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self, text="WELCOME", font="Arial 20 bold", bg='#4F4A45', foreground="#ED7D31")
        self.welcome_label.place(x=125, y=20)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.place(x=10, y=120)
        self.email_entry = tk.Entry(self, border=1)
        self.email_entry.place(x=55, y=121)

        self.pass_label = tk.Label(self, text="Password:")
        self.pass_label.place(x=10, y=170)
        self.pass_entry = tk.Entry(self, border=1)
        self.pass_entry.place(x=75, y=171)

        self.back_button = tk.Button(self, text="back", command=self.go_to_welcome_page)
        self.back_button.place(x=30, y=550)

        self.continue_button = tk.Button(self, text='Login', command=self.go_to_BMI_Page)
        self.continue_button.place(x=70, y=550)

        self.forgot_password_button = tk.Button(self, text = 'Forgot your password?', bd = 0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x= 30, y=400)

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

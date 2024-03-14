import tkinter as tk

class Login (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=500)
    
        #ANGELAINE NEW
        self.login_bg = tk.Frame(self, bg='#7B6079', height=500, width=450)
        self.login_bg.place(x=0, y=0)

<<<<<<< HEAD
        self.welcome_label = tk.Label(self.login_bg, text="WELCOME", font=('Courier', 25, 'bold'), fg='white', bg='#7B6079')
        self.welcome_label.place(x=150, y=40)

        self.email_label = tk.Label(self.login_bg, text="Email", font=('Courier', 15), fg='white', bg='#7B6079')
        self.email_label.place(x=100, y=145)

        self.email_entry = tk.Entry(self.login_bg, border=1, width=20, font=('Courier', 15), bg='#694e67')
        self.email_entry.place(x=100, y=170)
=======
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
>>>>>>> ffb308988368a98004e3e12caac8aec91ecda476

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='white', bg='#7B6079')
        self.pass_label.place(x=100, y=225)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=20, font=('Courier', 15), bg='#694e67')
        self.pass_entry.place(x=100, y=255)

        self.back_button = tk.Button(self.login_bg, text="BACK", width=13, font=('Courier', 15, 'bold'),bg='#FFE9D6',command=self.go_to_welcome_page)
        self.back_button.place(x=40, y=350)

        self.login_button = tk.Button(self.login_bg, text='Login', width=13, font=('Courier', 15, 'bold'),bg='#DE8971',command=self.go_to_BMI_Page)
        self.login_button.place(x=250, y=350)

        self.forgot_password_button = tk.Button(self.login_bg, text = 'Forgot your password?',  font=('Courier', 11), fg='#88f2ea', bg='#7B6079',bd = 0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=153, y=282)

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

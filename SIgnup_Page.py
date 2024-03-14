import tkinter as tk

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.create_account_bg = tk.Frame(self, bg='#4F4A45', height=600, width=400)
        self.create_account_bg.place(x=0, y=0)

        self.back_button = tk.Button(self, text="back", command=self.go_to_welcome_page)
        self.back_button.place(x=30, y=550)

        self.continue_button = tk.Button(self, text='Login', command=self.go_to_Login_Page)
        self.continue_button.place(x=70, y=550)

        self.create_account_label = tk.Label(self, text='Create an Account', font='Arial 20 bold', bg='#4F4A45', foreground="#ED7D31")
        self.create_account_label.place(x=75, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font='Arial 16',  bg='#4F4A45', foreground="#ED7D31")
        self.to_get_started_label.place(x=130, y=40)

        self.first_name_label = tk.Label(self, text='First Name')
        self.first_name_label.place(x=10, y=100)

        self.first_name_entry = tk.Entry(self, border=1)
        self.first_name_entry.place(x=80, y=100)

        self.last_name_label = tk.Label(self, text='Last Name')
        self.last_name_label.place(x=10, y=135)

        self.last_name_entry = tk.Entry(self, border=1)
        self.last_name_entry.place(x=80, y=135)

        self.gmail_label = tk.Label(self, text='Gmail')
        self.gmail_label.place(x=10, y=170)

        self.gmail_entry = tk.Entry(self, border=1)
        self.gmail_entry.place(x=55, y=170)

        self.username_label = tk.Label(self, text='Username')
        self.username_label.place(x=10, y=205)

        self.username_entry = tk.Entry(self, border=1)
        self.username_entry.place(x=80, y=205)

        self.password_label = tk.Label(self, text='Password')
        self.password_label.place(x=10, y=240)

        self.password_entry = tk.Entry(self, border=1)
        self.password_entry.place(x=75, y=240)

        self.confirm_password_label = tk.Label(self, text='Confirm Password')
        self.confirm_password_label.place(x=10, y=275)

        self.confirm_password_entry = tk.Entry(self, border=1)
        self.confirm_password_entry.place(x=125, y=275)

        self.captcha_label = tk.Label(self, text='Captcha')
        self.captcha_label.place(x=10, y=310)

        self.terms_and_conditions_label = tk.Label(self, text='Terms & Conditions')
        self.terms_and_conditions_label.place(x=10, y=345)

        self.sign_up_button = tk.Button(self, text='Sign Up', height=1, width=50)
        self.sign_up_button.place(x=20, y=415)

        self.already_have_an_account_login = tk.Button(self, text='Already have an account? Login', height=1, width=50)
        self.already_have_an_account_login.place(x=20, y=455)








    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')


    def go_to_Login_Page(self):
        self.parent.change_window('Login')


    def on_return(self):
        pass
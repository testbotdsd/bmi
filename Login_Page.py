import tkinter as tk

class Login (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=595)
    
        #ANGELAINE NEW
        self.login_bg = tk.Frame(self, bg='#7B6079', height=595, width=450)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self.login_bg, text="WELCOME", font=('Courier', 45, 'bold'), fg='white', 
                                      bg='#7B6079')
        self.welcome_label.place(x=95, y=40)

        self.email_label = tk.Label(self.login_bg, text="Username", font=('Courier', 15), fg='white', bg='#7B6079')
        self.email_label.place(x=100, y=145)

        self.email_entry = tk.Entry(self.login_bg, border=1, width=20, font=('Courier', 15), bg='#694e67')
        self.email_entry.place(x=100, y=170)

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='white', bg='#7B6079')
        self.pass_label.place(x=100, y=225)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=20, font=('Courier', 15), bg='#694e67')
        self.pass_entry.place(x=100, y=255)

        self.back_button = tk.Button(self.login_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'),bg='#FFE9D6',command=self.go_to_welcome_page)
        self.back_button.place(x=5, y=10)

<<<<<<< HEAD
        self.login_button = tk.Button(self.login_bg, text='LOGIN', width=23, font=('Courier', 15, 'bold'),bg='#DE8971',
                                      command=self.go_to_BMI_Page)
        self.login_button.place(x=80, y=444)
=======
        self.login_button = tk.Button(self.login_bg, text='LOGIN', width=19, font=('Courier', 15, 'bold'),bg='#DE8971',command=self.go_to_BMI_Page)
        self.login_button.place(x=100, y=444)
>>>>>>> a55d978cb1ef889c30fe532887fde229f2e21a17

        self.forgot_password_button = tk.Button(self.login_bg, text = 'Forgot your password?',  font=('Courier', 11), fg='#88f2ea', bg='#7B6079',bd = 0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=153, y=282)

        self.no_account_label = tk.Label(self, text="Don't have an account?", bg='#7B6079', font="Courier 10", foreground='white')
        self.no_account_label.place(x=82, y=488)

<<<<<<< HEAD
        self.sign_up_btn = tk.Button(self, text="Sign up now", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), 
                                     command=self.go_to_signup, foreground='#88f2ea')
        self.sign_up_btn.place(x=264, y=487)
=======
        self.sign_up_btn = tk.Button(self, text="Sign up now", bg='#7B6079', bd=0, font=('Courier', 8, 'bold'), command=self.go_to_signup, foreground='#88f2ea')
        self.sign_up_btn.place(x=259, y=488)
>>>>>>> a55d978cb1ef889c30fe532887fde229f2e21a17

    def go_to_forgot_password(self):
        self.parent.change_window('Forgot_Password')

    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')

    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')
    
    def go_to_signup(self):
        self.parent.change_window('Signup')

class Forgot_Password (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)

        self.login_bg = tk.Frame(self, bg='#7B6079', height=595, width=450)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self.login_bg, text="FORGOT PASSWORD", font=('Courier', 20, 'bold'), fg='white', bg='#7B6079')
        self.welcome_label.place(x=95, y=40)

        self.back_button = tk.Button(self.login_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'),bg='#FFE9D6')
        self.back_button.place(x=5, y=10)

    def go_to_login(self):
        self.parent.change_window('Login')
    
    
    def on_return(self):
        pass

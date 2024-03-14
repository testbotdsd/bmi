import tkinter as tk

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=600)

        #WELCOME LABELS
        self.create_account_bg = tk.Frame(self, bg='#7B6079', height=600, width=450)
        self.create_account_bg.place(x=0, y=0)

        self.create_account_label = tk.Label(self, text='Create an Account', font=('Courier', 25, 'bold'), bg='#7B6079', foreground="white")
        self.create_account_label.place(x=25, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font=('Courier', 15, 'bold'),  bg='#7B6079', foreground="white")
        self.to_get_started_label.place(x=118, y=40)

        #INFORMATIONS
        self.first_name_label = tk.Label(self, text='First Name', font=('Courier', 13), fg='white', bg='#7B6079')
        self.first_name_label.place(x=81, y=75)

        self.first_name_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23)
        self.first_name_entry.place(x=81, y=99)

        self.last_name_label = tk.Label(self, text='Last Name', font=('Courier', 13), fg='white', bg='#7B6079')
        self.last_name_label.place(x=81, y=132)

        self.last_name_entry = tk.Entry(self, border=1, font=('Courier', 13),width=23)
        self.last_name_entry.place(x=81, y=156)

        self.gmail_label = tk.Label(self, text='Gmail', font=('Courier', 13), fg='white', bg='#7B6079')
        self.gmail_label.place(x=81, y=189)

        self.gmail_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23)
        self.gmail_entry.place(x=81, y=213)

        self.username_label = tk.Label(self, text='Username', font=('Courier', 13), fg='white', bg='#7B6079')
        self.username_label.place(x=81, y=246)

        self.username_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23)
        self.username_entry.place(x=81, y=270)

        self.password_label = tk.Label(self, text='Password', font=('Courier', 13), fg='white', bg='#7B6079')
        self.password_label.place(x=81, y=303)

        self.password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23)
        self.password_entry.place(x=81, y=327)

        self.confirm_password_label = tk.Label(self, text='Confirm Password', font=('Courier', 13), fg='white', bg='#7B6079')
        self.confirm_password_label.place(x=81, y=360)

        self.confirm_password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23)
        self.confirm_password_entry.place(x=81, y=384)
        
        self.birthday_label = tk.Label(self, text = 'Birthday', font=('Courier', 13), fg='white', bg='#7B6079')
        self.birthday_label.place(x=81, y=420)
        
        self.birthday_entry = tk.Entry(self, border=1, font=('Courier', 13))
        self.birthday_entry.place(x=170, y=420)  
        
        self.captcha_label = tk.Label(self, text='Captcha')
        self.captcha_label.place(x=189, y=460)

        self.terms_and_conditions_label = tk.Label(self, text='Terms & Conditions')
        self.terms_and_conditions_label.place(x=170, y=484)

        self.sign_up_button = tk.Button(self, text='Next', width=21, font=('Courier', 15, 'bold'),bg='#DE8971', command=self.go_to_Photo_page)
        self.sign_up_button.place(x=65, y=517)

        self.have_an_account_login_label = tk.Label(self, text='Already have an account?', bg='#7B6079', font="Courier 10", foreground='white')
        self.have_an_account_login_label.place(x=68, y=560)
        
        self.login_clickable = tk.Button(self, text="Login", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.login_clickable.place(x=275, y=559)


    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')

    def go_to_Photo_page(self):
        self.parent.change_window('Photo')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')


    def on_return(self):
        pass
    
class Photo (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        self.Photo_bg = tk.Frame(self, bg='#7B6079', height=600, width=450)
        self.Photo_bg.place(x=0, y=0)
        
        self.photo_label = tk.Label(self, text="photo")
        self.photo_label.place(x=50, y=100)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = tk.Button(self, text="Finish", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.Finish_button.place(x=275, y=559)
        
    def go_to_create_acc(self):
        self.parent.change_window('Signup')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')
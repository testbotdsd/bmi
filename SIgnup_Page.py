import tkinter as tk

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=595)

        #WELCOME LABELS

        self.create_account_bg = tk.Frame(self, bg='#7B6079', height=595, width=450)
        self.create_account_bg.place(x=0, y=0)

        self.create_account_label = tk.Label(self, text='Create an Account', font=('Courier', 25, 'bold'), bg='#7B6079', foreground="white")
        self.create_account_label.place(x=55, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font=('Courier', 15, 'bold'),  bg='#7B6079', foreground="white")
        self.to_get_started_label.place(x=148, y=40)

        #INFORMATIONS
        self.first_name_label = tk.Label(self, text='First Name', font=('Courier', 12), fg='white', bg='#7B6079')
        self.first_name_label.place(x=40, y=80)

        self.first_name_entry = tk.Entry(self, border=1, width=31)
        self.first_name_entry.place(x=40, y=104)

        self.last_name_label = tk.Label(self, text='Last Name', font=('Courier', 12), fg='white', bg='#7B6079')
        self.last_name_label.place(x=40, y=137)

        self.last_name_entry = tk.Entry(self, border=1, width=31)
        self.last_name_entry.place(x=40, y=161)

        self.gmail_label = tk.Label(self, text='Gmail', font=('Courier', 12), fg='white', bg='#7B6079')
        self.gmail_label.place(x=40, y=194)

        self.gmail_entry = tk.Entry(self, border=1, width=31)
        self.gmail_entry.place(x=40, y=218)

        self.username_label = tk.Label(self, text='Username', font=('Courier', 12), fg='white', bg='#7B6079')
        self.username_label.place(x=40, y=251)

        self.username_entry = tk.Entry(self, border=1, width=31)
        self.username_entry.place(x=40, y=275)

        self.password_label = tk.Label(self, text='Password', font=('Courier', 12), fg='white', bg='#7B6079')
        self.password_label.place(x=40, y=308)

        self.password_entry = tk.Entry(self, border=1, width=31)
        self.password_entry.place(x=40, y=332)

        self.confirm_password_label = tk.Label(self, text='Confirm Password', font=('Courier', 12), fg='white', bg='#7B6079')
        self.confirm_password_label.place(x=40, y=365)

        self.confirm_password_entry = tk.Entry(self, border=1, width=31)
        self.confirm_password_entry.place(x=40, y=389)

        self.captcha_label = tk.Label(self, text='Captcha')
        self.captcha_label.place(x=40, y=432)

        self.tnc_checkbox = tk.Checkbutton(self, text="I agree to the", bg='#7B6079', font="Courier 10", foreground='white')
        self.tnc_checkbox.place(x=40, y=475)

        self.terms_conditions_btn = tk.Button(self, text="Terms & Conditions",font=('Courier', 11), 
                                                fg='#88f2ea', bg='#7B6079',bd = 0)
        self.terms_conditions_btn.place(x=180, y=475)

        self.sign_up_button = tk.Button(self, text='Sign Up', width=21, font=('Courier', 15, 'bold'),bg='#DE8971', command=self.go_to_Login_Page)
        self.sign_up_button.place(x=90, y=517)

        self.have_an_account_login_label = tk.Label(self, text='Already have an account?', bg='#7B6079', font="Courier 10", foreground='white')
        self.have_an_account_login_label.place(x=93, y=560)
        
        self.login_clickable = tk.Button(self, text="Login", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.login_clickable.place(x=300, y=559)


    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')


    def go_to_Login_Page(self):
        self.parent.change_window('Login')


    def on_return(self):
        pass
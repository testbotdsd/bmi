import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
        
        # Adding a Birthday Picker using a Combobox
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()

        self.day_label = tk.Label(self, text="Day", font=('Courier', 10), fg='white', bg='#7B6079')
        self.day_label.place(x=81, y=444)
        self.day_combo = ttk.Combobox(self, textvariable=self.day_var, state='readonly', font=('Courier', 13), width=3)
        self.day_combo['values'] = [str(i) for i in range(1, 32)]
        self.day_combo.place(x=111, y=444)
        self.day_combo.current(0)

        self.month_label = tk.Label(self, text="Month", font=('Courier', 10), fg='white', bg='#7B6079')
        self.month_label.place(x=170, y=444)
        self.month_combo = ttk.Combobox(self, textvariable=self.month_var, state='readonly', font=('Courier', 13), width=3)
        self.month_combo['values'] = [str(i) for i in range(1, 13)]
        self.month_combo.place(x=220, y=444)
        self.month_combo.current(0)

        self.year_label = tk.Label(self, text="Year", font=('Courier', 10), fg='white', bg='#7B6079')
        self.year_label.place(x=280, y=444)
        self.year_combo = ttk.Combobox(self, textvariable=self.year_var, state='readonly', font=('Courier', 13), width=4)
        self.year_combo['values'] = [str(i) for i in range(1900, 2025)]
        self.year_combo.place(x=317, y=444)
        self.year_combo.current(0)

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
        
        self.photo_label = tk.Label(self, text="photo", font=('Courier', 20, 'bold'))
        self.photo_label.place(x=50, y=100)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = tk.Button(self, text='Finish', width=21, font=('Courier', 15, 'bold'),bg='#DE8971', command=self.go_to_Login_Page)
        self.Finish_button.place(x=65, y=517)
        
        self.captcha_label = tk.Label(self, text='Captcha')
        self.captcha_label.place(x=189, y=460)

        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable= self.terms_and_conditions_var)
        self.terms_and_conditions_check_button.place(x=95, y=484)
<<<<<<< HEAD
=======
        
    #     # self.terms_and_conditions_label = tk.Label(self, text='Terms & Conditions')
    #     # self.terms_and_conditions_label.place(x=170, y=484)
    # def go_to_terms_and_condition(self):
    #     if self.off_checkbox.get() == 'on':
    #         self.parent.change_window('Terms_And_Conditions')
    #     else:
    #         self.parent.change_window('Photo')
>>>>>>> c775daf60138db3276ca8cc608b56961331927cc

    def go_to_create_acc(self):
        self.parent.change_window('Signup')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')

    
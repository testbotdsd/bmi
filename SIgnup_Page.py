import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Model

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=600)

        #WELCOME LABELS
        self.create_account_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.create_account_bg.place(x=0, y=0)

        self.create_account_label = tk.Label(self, text='Create an Account', font=('Courier', 25, 'bold'),  fg='#EEEDEB', bg='#3C3633')
        self.create_account_label.place(x=55, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font=('Courier', 15, 'bold'),   fg='#EEEDEB', bg='#3C3633')
        self.to_get_started_label.place(x=130, y=50)

        #INFORMATIONS
        self.first_name_label = tk.Label(self, text='First Name', font=('Courier', 13),  fg='#EEEDEB', bg='#3C3633')
        self.first_name_label.place(x=45, y=120)

        self.first_name_entry = tk.Entry(self, border=1, font=('Courier', 13), width=17, bg='#59504b')
        self.first_name_entry.place(x=42, y=144)

        self.last_name_label = tk.Label(self, text='Last Name', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.last_name_label.place(x=235, y=120)

        self.last_name_entry = tk.Entry(self, border=1, font=('Courier', 13),width=17, bg='#59504b')
        self.last_name_entry.place(x=237, y=144)

        self.gmail_label = tk.Label(self, text='Gmail', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.gmail_label.place(x=100, y=189)

        self.gmail_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.gmail_entry.place(x=100, y=213)

        self.username_label = tk.Label(self, text='Username', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=100, y=246)

        self.username_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.username_entry.place(x=100, y=270)

        self.password_label = tk.Label(self, text='Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.password_label.place(x=100, y=303)

        self.password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.password_entry.place(x=100, y=327)

        self.confirm_password_label = tk.Label(self, text='Confirm Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.confirm_password_label.place(x=100, y=360)

        self.confirm_password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=23, bg='#59504b')
        self.confirm_password_entry.place(x=100, y=384)
        
        self.birthday_label = tk.Label(self, text = 'Birthday', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=90, y=420) 

        # Adding a Birthday Picker using a Combobox
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()

        self.day_label = tk.Label(self, text="Day", font=('Courier', 10),  fg='#EEEDEB', bg='#3C3633')
        self.day_label.place(x=81, y=444)
        self.day_combo = ttk.Combobox(self, textvariable=self.day_var, state='readonly', font=('Courier', 13), width=3)
        self.day_combo['values'] = [str(i) for i in range(1, 32)]
        self.day_combo.place(x=111, y=444)
        self.day_combo.current(0)

        self.month_label = tk.Label(self, text="Month", font=('Courier', 10),  fg='#EEEDEB', bg='#3C3633')
        self.month_label.place(x=170, y=444)
        self.month_combo = ttk.Combobox(self, textvariable=self.month_var, state='readonly', font=('Courier', 13), width=3)
        self.month_combo['values'] = [str(i) for i in range(1, 13)]
        self.month_combo.place(x=220, y=444)
        self.month_combo.current(0)

        self.year_label = tk.Label(self, text="Year", font=('Courier', 10),  fg='#EEEDEB', bg='#3C3633')
        self.year_label.place(x=280, y=444)
        self.year_combo = ttk.Combobox(self, textvariable=self.year_var, state='readonly', font=('Courier', 13), width=4)
        self.year_combo['values'] = [str(i) for i in range(1900, 2025)]
        self.year_combo.place(x=317, y=444)
        self.year_combo.current(0)

        self.have_an_account_login_label = tk.Label(self, text='Already have an account?', bg='#3C3633', font="Courier 10", foreground='white')
        self.have_an_account_login_label.place(x=100, y=560)

        self.sign_up_button = tk.Button(self, text='Continue', width=21, font=('Courier', 15, 'bold'),bg='#d3d3d3', command=self.validate_sign_up)
        self.sign_up_button.place(x=85, y=517)
        
        self.login_clickable = tk.Button(self, text="Login", fg='#EEEDEB', bg='#3C3633' , bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.login_clickable.place(x=295, y=559)

    def validate_sign_up(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gmail = self.gmail_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if first_name == '':
            messagebox.showerror('Sign in', 'First name field is empyt, please fill it out.')
            return False
        
        if last_name == '':
            messagebox.showerror('Sign in', 'Last name field is empyt, please fill it out.')
            return False
        
        if gmail == '':
            messagebox.showerror('Sign in', 'Gmail field is empyt, please fill it out.')
            return False
        
        if username == '':
            messagebox.showerror('Sign in', 'Username field is empyt, please fill it out.')
            return False
        
        if password == '':
            messagebox.showerror('Sign in', 'Password field is empyt, please fill it out.')
            return False
        
        if confirm_password == '':
            messagebox.showerror('Sign in', 'Confirm password field is empyt, please fill it out.')
            return False
        
        else:
            self.go_to_Photo_page()
        
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
        
        self.Photo_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.Photo_bg.place(x=0, y=0)
        
        self.photo_label = tk.Label(self, text="photo", font=('Courier', 20, 'bold'))
        self.photo_label.place(x=50, y=100)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = tk.Button(self, text='Finish', width=21, font=('Courier', 15, 'bold'), bg='#d3d3d3', command=self.go_to_Login_Page)
        self.Finish_button.place(x=65, y=517)
        
        self.captcha_label = tk.Label(self, text='Captcha', font=('Courier', 12, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.captcha_label.place(x=160, y=240)

        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable= self.terms_and_conditions_var, command=self.terms_conditios_var)
        self.terms_and_conditions_check_button.place(x=95, y=484)

        self.generate_captcha_button = tk.Button(self, text="Generate Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3', command=self.generate_captcha)
        self.generate_captcha_button.place(x=110, y=275)

        self.captcha_label = tk.Label(self, text='', font=("Arial", 12), width=10)
        self.captcha_label.place(x=150, y=325)
            
        self.captcha = tk.Label(self, text="Enter Captcha", font=('Courier', 12, 'bold'), bg='#d3d3d3')
        self.captcha.place(x=130, y=375)
        self.captcha_input = tk.Entry(self, text="Enter Captcha here", width=20)
        self.captcha_input.place(x=135, y=425)

    def generate_captcha(self):
        captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.captcha_label.config(text=captcha)

    def terms_conditios_var(self):
        if self.terms_and_conditions_var.get():
            result = messagebox.askokcancel("Terms and condition", "Do you accept the Terms and Conditions?")
            if result:
                 pass
            else:
                self.terms_and_conditions_var.set(False)
        

    def go_to_create_acc(self):
        self.parent.change_window('Signup')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')

    
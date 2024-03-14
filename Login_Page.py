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

        self.username_label = tk.Label(self.login_bg, text="Username", font=('Courier', 15), fg='white', bg='#7B6079')
        self.username_label.place(x=81, y=185)

        self.username_entry = tk.Entry(self.login_bg, border=1, width=23, font=('Courier', 15), bg='#694e67')
        self.username_entry.place(x=81, y=215)

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='white', bg='#7B6079')
        self.pass_label.place(x=81, y=265)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=23, font=('Courier', 15), bg='#694e67')
        self.pass_entry.place(x=81, y=295)

        self.back_button = tk.Button(self.login_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'),
                                     bg='#FFE9D6',command=self.go_to_welcome_page)
        self.back_button.place(x=5, y=5)

        self.login_button = tk.Button(self.login_bg, text='LOGIN', width=23, font=('Courier', 15, 'bold'),bg='#DE8971',
                                      command=self.go_to_BMI_Page)
        self.login_button.place(x=80, y=444)

        self.forgot_password_button = tk.Button(self.login_bg, text = 'Forgot your password?',  font=('Courier', 11), 
                                                fg='#88f2ea', bg='#7B6079',bd = 0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=166, y=322)

        self.no_account_label = tk.Label(self, text="Don't have an account?", bg='#7B6079', font="Courier 10", foreground='white')
        self.no_account_label.place(x=82, y=488)

        self.sign_up_btn = tk.Button(self, text="Sign up now", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), 
                                     command=self.go_to_signup, foreground='#88f2ea')
        self.sign_up_btn.place(x=264, y=487)

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

        self.forgot_password_label_bg = tk.Frame(self, bg='#7B6079', height=600, width=450)
        self.forgot_password_label_bg.place(x=0, y=0)

        self.forgot_password_label = tk.Label(self.forgot_password_label_bg, text="Forgot Password", font=('Courier', 20, 'bold'), fg='white', bg='#7B6079')
        self.forgot_password_label.place(x = 40, y = 30)

        # gmail num
        self.gmail_num_label = tk.Label(self.forgot_password_label_bg, text="GMAIL NUMBER", font=('Courier', 15), fg='white', bg='#7B6079')
        self.gmail_num_label.place(x = 100, y= 110)
        
        self.gmail_num_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12))
        self.gmail_num_entry.place(x= 100, y= 145)

        #new pass
        self.new_password_label = tk.Label(self.forgot_password_label_bg, text="NEW PASSWORD", font=('Courier', 15), fg='white', bg='#7B6079')
        self.new_password_label.place( x = 100, y= 190)
        
        self.new_password_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), show='*')
        self.new_password_entry.place(x = 100, y= 225)

        #conf pass
        self.confirm_password_label = tk.Label(self.forgot_password_label_bg, text="CONFIRM PASSWORD", font=('Courier', 15), fg='white', bg='#7B6079')
        self.confirm_password_label.place(x= 100, y= 270)
        
        self.confirm_password_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12), show='*')
        self.confirm_password_entry.place(x = 100, y = 305)
        
        #verification
        self.verification_label = tk.Label(self.forgot_password_label_bg, text="VERIFICATION", font=('Courier', 15), fg='white', bg='#7B6079')
        self.verification_label.place(x= 100, y= 350)
        
        self.verification_entry = tk.Entry(self.forgot_password_label_bg, font=('Courier', 12))
        self.verification_entry.place(x = 100, y = 385)

        #cont button
        self.continue_button = tk.Button(self.forgot_password_label_bg, text="CONTINUE", font=('Courier', 12), fg='white', bg='#7B6079', command=self.go_to_login)
        self.continue_button.place( x =150, y = 440)

        #back button
        self.back_button = tk.Button(self.forgot_password_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

    def go_to_login(self):
        self.parent.change_window('Login')
    
    def on_return(self):
        pass

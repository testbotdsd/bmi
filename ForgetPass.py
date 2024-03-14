import tkinter as tk

class Forgot_Password(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=450, height=600)

        self.forgot_pass_label_bg = tk.Frame(self, bg='#7B6079', height=600, width=450)
        self.forgot_pass_label_bg.place(x=0, y=0)

        self.forgot_pass_label = tk.Label(self.forgot_pass_label_bg, text="Forgot Password", font=('Courier', 20, 'bold'), fg='white', bg='#7B6079')
        self.forgot_pass_label.place(x = 40, y = 30)

        # gmail num
        self.gmail_num_label = tk.Label(self.forgot_pass_label_bg, text="GMAIL NUMBER", font=('Courier', 15), fg='white', bg='#7B6079')
        self.gmail_num_label.place(x = 100, y= 110)
        
        
        self.gmail_num_entry = tk.Entry(self.forgot_pass_label_bg, font=('Courier', 12))
        self.gmail_num_entry.place(x= 100, y= 145)

        #verifcation
        self.verification_label = tk.Label(self.forgot_pass_label_bg, text="VERIFICATION CODE", font=('Courier', 15), fg='white', bg='#7B6079')
        self.verification_label.place(x= 100, y= 190)
        
        
        self.verification_entry = tk.Entry(self.forgot_pass_label_bg, font=('Courier', 12))
        self.verification_entry.place(x =100, y= 225)

        #new pass
        self.new_password_label = tk.Label(self.forgot_pass_label_bg, text="NEW PASSWORD", font=('Courier', 15), fg='white', bg='#7B6079')
        self.new_password_label.place( x = 100, y= 270)
        
        
        self.new_password_entry = tk.Entry(self.forgot_pass_label_bg, font=('Courier', 12), show='*')
        self.new_password_entry.place(x = 100, y= 305)

        #conf pass
        self.confirm_password_label = tk.Label(self.forgot_pass_label_bg, text="CONFIRM PASSWORD", font=('Courier', 15), fg='white', bg='#7B6079')
        self.confirm_password_label.place(x= 100, y= 350)
        
        
        self.confirm_password_entry = tk.Entry(self.forget_pass_label_bg, font=('Courier', 12), show='*')
        self.confirm_password_entry.place(x = 100, y = 385)

        #cont button
        self.continue_button = tk.Button(self.forgot_pass_label_bg, text="CONTINUE", font=('Courier', 12), fg='white', bg='#7B6079')
        self.continue_button.place( x =150, y = 440)

        #back button
        self.back_button = tk.Button(self.forgpt_pass_label_bg, text="←", width=4, height=1, font=('Courier', 12, 'bold'), bg='#FFE9D6', command=self.go_to_login)
        self.back_button.place(x= 5, y= 10)

        
        
        
        
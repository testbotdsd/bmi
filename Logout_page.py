import tkinter as tk

class Logout(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)
        
        self.profile_bg = tk.Frame(self, bg='#7B6079', height=600, width=450)
        self.profile_bg.place(x=0, y=0)

        self.profile_label = tk.Label(self, text='Profile', font='Arial 20 bold', bg='#4F4A45', foreground="#ED7D31")
        self.profile_label.place(x=180, y=10)

        self.picture_label = tk.Label(self, text= 'Picture')
        self.picture_label.place(x=10, y=100)

        self.name_label = tk.Label(self, text= 'Name')
        self.name_label.place(x=10, y=150)

        self.birthday_label = tk.Label(self, text='Birthday')
        self.birthday_label.place(x=10, y=200)

        self.information_label = tk.Label(self, text='Information')
        self.information_label.place(x=10, y=250)
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_BMI_page)
        self.Back_button.place(x=5, y=5)

        self.log_out_button = tk.Button(self, text='Logout', height=1, width=60, command=self.go_to_login_page)
        self.log_out_button.place(x=10, y=350)
        
    def go_to_BMI_page(self):
        self.master.change_window('BMI')  
        
    def go_to_login_page(self):
        self.master.change_window('Login')
        
    def on_return(self):
        pass

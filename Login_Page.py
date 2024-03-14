import tkinter as tk

class Login (tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        

        #ANGELAINE NEW
        self.welcome_label = tk.Label(self, text="WELCOME", font="Arial 20 bold")
        self.welcome_label.place(x=0, y=0)

        self.email_entry = tk.Entry(self, border=1)
        self.email_entry.place(x=10, y=50)

        self.back_button = tk.Button(self, text="back", command=self.go_to_welcome_page)
        self.back_button.place(x=30, y=550)

        self.continue_button = tk.Button(self, text='Login', command=self.go_to_BMI_Page)
        self.continue_button.place(x=70, y=550)


    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')


    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')


    def on_return(self):
        pass

import tkinter as tk

class Welcome(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=350, height=400)

        self.login_bg = tk.Frame(self, bg='#4F4A45', height=400, width=350)
        self.login_bg.place(x=0, y=0)

        # self.background_image = tk.PhotoImage(file="login picture.png")
        # self.resized_background_image = self.background_image.subsample(2,2)
        # self.background_label = tk.Label(self, image=self.resized_background_image)
        # self.background_label.place(relwidth=1, relheight=1)

        self.welcome1_label = tk.Label(self, text="WELCOME TO", font="Arial 25 bold", bg='#4F4A45', 
                                      foreground='#ED7D31')
        self.welcome1_label.place(x=57, y=40)
        self.welcome2_label = tk.Label(self, text="BMI CALCULATOR", font="Arial 25 bold", bg='#4F4A45', 
                                      foreground='#ED7D31')
        self.welcome2_label.place(x=20, y=80)

        self.login_btn = tk.Button(self, text="Login", font="Garamond 12 bold", width=12, command=self.go_to_login_page)
        self.login_btn.place(x=110, y=195)

        self.sign_up_btn = tk.Button(self, text="Signup", font="Garamond 12 bold", width=12)
        self.sign_up_btn.place(x=110, y=255)
        

    def go_to_login_page(self):
        self.master.change_window('Login')
        
    def on_return(self):
        pass

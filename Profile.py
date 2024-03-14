import tkinter as tk

class Profile(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")
        self.geometry('450x600')
        self.wm_resizable(False, False)

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

        self.log_out_button = tk.Button(self, text='Logout', height=1, width=60)
        self.log_out_button.place(x=10, y=350)

root = Profile()
root.mainloop()



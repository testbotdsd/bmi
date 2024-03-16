import tkinter as tk

class Profile(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        self.profile_bg = tk.Frame(self, bg='#3C3633', height=600, width=400)
        self.profile_bg.place(x=0, y=0)

        self.logout_button = tk.Button(self, text = 'Logout', font=('Courier', 15, 'bold'), bg='#E0CCBE', foreground='#3C3633', 
                                        relief="raised", width=16, command=self.go_to_main_page)
        self.logout_button.place(x=10, y=10)
        
    def go_to_main_page(self):
        self.parent.change_window('Welcome_Page')

    def on_return(self):
        pass

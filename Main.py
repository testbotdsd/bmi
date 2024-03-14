import tkinter as tk
import Welcome_Page
import Login_Page
import BMI_Page
import SIgnup_Page

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")     

        self.frames = {}
        self.frames ['Welcome_Page'] = Welcome_Page.Welcome(self)

        self.frames ['Login'] = Login_Page.Login(self)
        self.frames ['Signup'] = SIgnup_Page.Signup(self)

        self.frames ['BMI'] = BMI_Page.BMI(self)


        self.change_window('Welcome_Page')

    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        
        self.frames[name].grid()

root = MainWindow()
root.resizable(False, False)
root.mainloop()

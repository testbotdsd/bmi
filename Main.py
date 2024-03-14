import tkinter as tk
import Welcome_Page
import Login_Page
import BMI_Page

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")     
        
        self.frames = {}
        self.frames['Front_Page'] = Welcome_Page.Welcome(self)

        self.frames['Login_Page'] = Login_Page.Login(self)

        self.frames['BMI_Page'] = BMI_Page.BMI(self)
        

        self.change_window('Front_Page')
        
    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        
        self.frames[name].grid()

root = MainWindow()
root.resizable(False, False)
root.mainloop()

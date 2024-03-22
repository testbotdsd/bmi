import tkinter as tk
import Welcome_Page
import Login_Page
import BMI_Page
import SIgnup_Page
import OTP_Page
import New_Password_Page

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")
        self.logged_in_user_id = None

        self.frames = {}
        self.frames ['Welcome_Page'] = Welcome_Page.Welcome(self)

        #login Page
        self.frames ['Login'] = Login_Page.Login(self)

        #Send OTP
        self.frames ['Forget'] = OTP_Page.Forget(self)
        
        #Change Password
        self.frames ['Reset_Password'] = New_Password_Page.Reset_Password(self)

        #Sign Up
        self.frames ['Signup'] = SIgnup_Page.Signup(self)
        self.frames ['Photo'] = SIgnup_Page.Photo(self, self.frames['Signup'])
        
        #BMI
        self.frames ['BMI'] = BMI_Page.BMI(self)

        self.change_window('Photo')

    def set_logged_in_user_id(self, user_id):
        self.logged_in_user_id = user_id

    def get_logged_in_user_id(self):
        return self.logged_in_user_id

    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        
        self.frames[name].grid()

    def change_window(self, name, **kwargs):
        for frame in self.frames.values():
            frame.grid_forget()
        self.frames[name].on_return(**kwargs)
        self.frames[name].grid()

    def on_return(self, **kwargs):
        pass
    
root = MainWindow()
root.resizable(False, False)
root.mainloop()



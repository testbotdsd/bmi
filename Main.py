import tkinter as tk
import Welcome_Page
import Login_Page
import BMI_Page
import SIgnup_Page
import Logout_page
import Profile_Page



class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("BMI CALCULATOR")

        self.frames = {}
        self.frames ['Welcome_Page'] = Welcome_Page.Welcome(self)

        #login Page
        self.frames ['Login'] = Login_Page.Login(self)
        self.frames ['Forgot_Password'] = Login_Page.Forgot_Password(self)

        #Sign Up
        self.frames ['Signup'] = SIgnup_Page.Signup(self)
        self.frames ['Photo'] = SIgnup_Page.Photo(self)

        #Profile Page
        self.frames ['Profile'] = Profile_Page.Profile(self)
        
        self.frames ['BMI'] = BMI_Page.BMI(self)
        
        self.frames ['Logout'] = Logout_page.Logout(self)

        self.change_window('Welcome_Page')

    def change_window(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        
        self.frames[name].grid()

    def update_content(self):
        # Get the updated window size
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        # Print the updated window size (you can replace this with your content update logic)
        print(f"Window size updated: {window_width} x {window_height}")

root = MainWindow()
root.resizable(True, True)

# Bind the window resize event to the update_content method
root.bind("<Configure>", lambda event: root.update_content())
root.mainloop()

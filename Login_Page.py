import tkinter as tk
from tkinter import messagebox
from customtkinter import *
import random
import string
import SIgnup_Page
import Data_base_Handler
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk

INITIAL_DELAY = 10000
SUBSEQUENT_DELAY = 10000

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=450, height=600)
    
        self.login_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.login_bg.place(x=0, y=0)

        self.welcome_label = tk.Label(self.login_bg, text="WELCOME", font=('Courier', 45, 'bold'), fg='#EEEDEB', bg='#3C3633')
        self.welcome_label.place(x=95, y=30)

        self.username_label = tk.Label(self.login_bg, text="Username", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=81, y=124)

        self.username_entry = tk.Entry(self.login_bg, border=1, width=23, font=('Courier', 15),fg='white', bg='#59504b')
        self.username_entry.place(x=81, y=158)

        self.pass_label = tk.Label(self.login_bg, text="Password", font=('Courier', 15), fg='#EEEDEB', bg='#3C3633')
        self.pass_label.place(x=81, y=211)

        self.pass_entry = tk.Entry(self.login_bg, border=1, width=19, font=('Courier', 15), fg='white', bg='#59504b', show='*')
        self.pass_entry.place(x=81, y=245)

        self.eye_hide = Image.open("hide.jpg")
        self.eye_hide = self.eye_hide.resize((22, 22))  
        self.eye_hide = ImageTk.PhotoImage(self.eye_hide) 

        self.eye_show = Image.open("show.jpg")
        self.eye_show = self.eye_show.resize((22, 22))  
        self.eye_show = ImageTk.PhotoImage(self.eye_show)

        self.toggle_password_button = tk.Button(self.login_bg, bd=1, bg='white', image=self.eye_show, command=self.toggle_password)
        self.toggle_password_button.place(x=322, y=246)


        self.forgot_password_button = tk.Button(self.login_bg, text='Forgot your password?',  font=('Courier', 11), fg='#5e918e', 
                                                bg='#3C3633', bd=0, command=self.go_to_forgot_password)
        self.forgot_password_button.place (x=166, y=283)

        self.login_button = CTkButton(self.login_bg, text='LOGIN', width=300,height=40,corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', 
                                        text_color='black',command=self.login_button_command)
        self.login_button.place(x=80, y=510)

        self.no_account_label = tk.Label(self.login_bg, text="Don't have an account?", bg='#3C3633', font="Courier 10", foreground='#EEEDEB')
        self.no_account_label.place(x=82, y=558)

        self.sign_up_btn = tk.Button(self.login_bg, text="Sign up now", bg='#3C3633', bd=0, font=('Courier', 10, 'bold'), 
                                        command=self.go_to_signup, foreground='#5e918e')
        self.sign_up_btn.place(x=264, y=557)

        self.password_hidden = True 

        self.terms_accepted = tk.IntVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable=self.terms_accepted,  
                                                                command=self.terms_conditions_var)
        self.terms_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button.place(x=115, y=470)

        self.terms_conditions_window = None 

        img=self.generate_captha()
        self.pic_frame = tk.Label(self, image=img)
        self.pic_frame.image = img  
        self.pic_frame.place(x=81, y=335)

        self.create_refresh_button()
        self.disable_retry_button()
        self.parent.after(INITIAL_DELAY, self.enable_retry_button)

        self.captcha_entry = tk.Entry(self.login_bg, border=1, width=20, font=('Courier', 15), fg='white', bg='#59504b')
        self.captcha_entry.place(x=81, y=405)

        self.captcha_window = None
        self.captcha_label_in_window = None

    def create_refresh_button(self):
        # Create the refresh button with appropriate callback
        self.refresh_img = Image.open("retry_icon.jpg")
        self.refresh_img = self.refresh_img.resize((25, 25))
        self.refresh_icon = ImageTk.PhotoImage(self.refresh_img)
        self.rfrsh_btn = tk.Button(self, image=self.refresh_icon, highlightbackground='#DE8971', highlightcolor='#DE8971',
                                    border=0, command=self.generate_captcha)
        self.rfrsh_btn.place(x=335, y=404)

    def enable_retry_button(self):
        self.rfrsh_btn.config(state='normal')

    def disable_retry_button(self):
        # Disable the refresh button
        self.rfrsh_btn.config(state='disabled')

    def generate_captcha(self):
        self.disable_retry_button()

        img = self.generate_captha()

        self.pic_frame.config(image=img)
        self.pic_frame.image = img
        self.parent.after(SUBSEQUENT_DELAY, self.enable_retry_button)

    def generate_captha(self):
        self.generated = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        captcha = ImageCaptcha(width=280, height=55)
        captcha_text = f'{self.generated}'
        img_data = captcha.generate(captcha_text)
        pil_image = Image.open(img_data)
        pil_image = pil_image.resize((280, 55))

        img = ImageTk.PhotoImage(pil_image)

        return img
    
    def login_button_command(self):
        if self.validate_captcha():
            self.validate_login()
    
    def validate_captcha(self):
        captcha = self.captcha_entry.get()
        if captcha == '':
            messagebox.showerror("Error", "Please input the CAPTCHA.")
            return False
        if captcha == self.generated:
            return True
        else:
            messagebox.showerror("Error", "Incorrect CAPTCHA.")
            return False
        
    def terms_conditions_var(self):
        result = messagebox.askokcancel("Terms and condition", "Do you accept the Terms and Conditions?")
        if result:
            self.terms_accepted.set(1)
        else:
            self.terms_accepted.set(0)

    def toggle_password(self):
        if self.password_hidden:
            self.password_entry.config(show='')
            self.show_pass.config(bg='#3C3633', fg='white', image=self.eye_hide)
            self.password_hidden = False
        else:
            self.password_entry.config(show='*')
            self.show_pass.config(bg='white', fg='#3C3633', image=self.eye_show)
            self.password_hidden = True

    def go_to_forgot_password(self):
        self.parent.change_window('Forget')
        self.generate_captcha()

    def go_to_BMI_Page(self):
        self.parent.change_window('BMI')
    
    def go_to_signup(self):
        self.parent.frames['Signup'].Bday_calendar_entry.delete(0, tk.END)
        self.parent.change_window('Signup')
        
        self.generate_captcha()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()

        if not self.terms_accepted.get():
            messagebox.showerror("Error", "Please accept the Terms and Conditions.")
            return

        dbconn = Data_base_Handler.database()
        user_id = dbconn.check_credentials(username, password)
        if user_id:
            self.parent.set_logged_in_user_id(user_id)
            self.reset_fields()
            login = messagebox.askyesno("BMI Login", "Are you sure you want to login?")
            if login == True:
                self.parent.change_window('BMI')
                self.generate_captcha()
        else:
            messagebox.showerror("Error", "Incorrect username or password.")

        dbconn.conn.close()

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.captcha_entry.delete(0, tk.END)

    def terms_conditions_var(self):
        if self.terms_accepted.get() == 1:
            if self.terms_conditions_window is None:
                self.create_terms_conditions_window()
            else:
                self.terms_conditions_window.deiconify()  
        else:
            if self.terms_conditions_window is not None:
                self.terms_conditions_window.destroy()  
                self.terms_conditions_window = None  
                self.terms_and_conditions_check_button.deselect()  

    def create_terms_conditions_window(self):
        self.terms_conditions_window = tk.Toplevel(self)
        self.terms_conditions_window.title("TERMS AND CONDITIONS")
        self.terms_conditions_window.geometry("450x600") 
        self.terms_conditions_window.resizable(False, False)
        self.terms_conditions_window.configure(bg='#3C3633')  

        scroll_frame = tk.Frame(self.terms_conditions_window)
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        scroll_bar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas = tk.Canvas(scroll_frame, yscrollcommand=scroll_bar.set, bg='#3C3633')
        canvas.pack(fill=tk.BOTH, expand=True)

        scroll_bar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll_bar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        terms_text = """
                                                                Terms and Conditions for BMI Calculator:


1. Use of the BMI Calculator:
By using the BMI Calculator provided in this application, you agree to abide by the following terms and conditions.

2. Accuracy of Results:
The BMI Calculator provides an estimate of your Body Mass Index (BMI) based on the information you input, including height, weight, age, and gender. It is important to note that BMI calculations are indicative and may not accurately reflect individual health conditions such as muscle mass, bone density, or specific medical conditions. Always consult with a healthcare professional for personalized health advice.

3. Personal Data:
The BMI Calculator may require you to input personal data such as height, weight and age. This information is used solely for the purpose of calculating BMI and is not stored or shared with third parties without your explicit consent. 

4. Health Disclaimer:
The BMI Calculator is intended for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. It is not designed to diagnose, treat, cure, or prevent any disease or health condition. Any reliance you place on BMI calculations is at your own risk. Always seek the advice of your physician or other qualified healthcare provider with any questions you may have regarding a medical condition.

5. Limitation of Liability:
We make no warranties or representations about the accuracy, reliability, completeness, or timeliness of the BMI Calculator or any results obtained from its use. We shall not be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in connection with the use of the BMI Calculator, including but not limited to lost profits, business interruption, or loss of data.

6. Acceptance of Terms:
By using the BMI Calculator, you acknowledge that you have read, understood, and agreed to these terms and conditions. If you do not agree with any part of these terms, please refrain from using the BMI Calculator.

7. Updates to Terms:
We reserve the right to update or modify these terms and conditions at any time without prior notice. It is your responsibility to review these terms periodically for changes. Continued use of the BMI Calculator after such changes constitutes acceptance of the updated terms.


Thank you for using our BMI Calculator and complying with these terms and conditions.
        """

        tk.Label(inner_frame, text=terms_text, justify=tk.LEFT, wraplength=400, bg='#3C3633', fg='white', font=('Courier', 10)).pack() 

        inner_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox(tk.ALL))

        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        ok_button = tk.Button(self.terms_conditions_window, text="Okay", font=('Courier', 10, 'bold'),bg='#d3d3d3', command=self.ok_action)
        ok_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        cancel_button = tk.Button(self.terms_conditions_window, text="Cancel", font=('Courier', 10, 'bold'),bg='#d3d3d3', command=self.cancel_action)
        cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def ok_action(self):
        self.terms_conditions_window.destroy() 

    def cancel_action(self):
        self.terms_conditions_window.destroy()  
        self.terms_and_conditions_check_button.deselect()  
        self.terms_conditions_window = None  
    
    def on_return(self):
        pass
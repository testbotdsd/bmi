import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *
import Model
import Data_base_Handler
import random
import string
from captcha.image import ImageCaptcha
import random
from tkcalendar import DateEntry
from datetime import date
from PIL import Image, ImageTk
import re
from io import BytesIO

INITIAL_DELAY = 10000
SUBSEQUENT_DELAY = 10000

class Signup(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__ (self, master)
        self.parent = master
        self.config(width=450, height=600)

        #WELCOME LABELS
        self.create_account_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.create_account_bg.place(x=0, y=0)

        self.create_account_label = tk.Label(self, text='Create an Account', font=('Courier', 25, 'bold'),  fg='#EEEDEB', bg='#3C3633')
        self.create_account_label.place(x=55, y=10)

        self.to_get_started_label = tk.Label(self, text='to get started', font=('Courier', 15, 'bold'),   fg='#EEEDEB', bg='#3C3633')
        self.to_get_started_label.place(x=130, y=50)

        #INFORMATIONS
        self.first_name_label = tk.Label(self, text='First Name', font=('Courier', 13),  fg='#EEEDEB', bg='#3C3633')
        self.first_name_label.place(x=70, y=90)

        self.first_name_entry = tk.Entry(self, border=1, font=('Courier', 13), width=30, bg='#59504b')
        self.first_name_entry.place(x=70, y=114)

        self.last_name_label = tk.Label(self, text='Last Name', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.last_name_label.place(x=70, y=147)

        self.last_name_entry = tk.Entry(self, border=1, font=('Courier', 13), width=30, bg='#59504b')
        self.last_name_entry.place(x=70, y=171)

        self.gmail_label = tk.Label(self, text='Gmail', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.gmail_label.place(x=70, y=266)

        self.gmail_entry = tk.Entry(self, border=1, font=('Courier', 13), width=30, bg='#59504b')
        self.gmail_entry.place(x=70, y=290)

        self.username_label = tk.Label(self, text='Username', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=70, y=323)

        self.username_entry = tk.Entry(self, border=1, font=('Courier', 13), width=30, bg='#59504b')
        self.username_entry.place(x=70, y=347)

        self.password_label = tk.Label(self, text='Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.password_label.place(x=70, y=380)

        self.password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=27, bg='#59504b', show="*")
        self.password_entry.place(x=70, y=404)

        self.confirm_password_label = tk.Label(self, text='Confirm Password', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.confirm_password_label.place(x=70, y=440)

        self.confirm_password_entry = tk.Entry(self, border=1, font=('Courier', 13), width=27, bg='#59504b', show="*")
        self.confirm_password_entry.place(x=70, y=464)

        self.birthday_label = tk.Label(self, text = 'Birthday', font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=70, y=205) 
    
        self.Bday_calendar_entry = DateEntry(self, width=47, background='Grey', foreground='white', borderwidth=2)
        self.Bday_calendar_entry.place (x=70, y=233)

        self.eye_hide = Image.open("hide.jpg")
        self.eye_hide = self.eye_hide.resize((21, 21))  
        self.eye_hide = ImageTk.PhotoImage(self.eye_hide) 

        self.eye_show = Image.open("show.jpg")
        self.eye_show = self.eye_show.resize((21, 21))  
        self.eye_show = ImageTk.PhotoImage(self.eye_show) 

        # Create the button with the loaded image
        self.show_pass = tk.Button(self, bd=1, bg='white', command=self.show_password, image=self.eye_show)
        self.show_pass.place(x=350, y=404)

        self.show_confirm_pass = tk.Button(self, bd=1, bg='white', command=self.confirm_password_show, image=self.eye_show)
        self.show_confirm_pass.place(x=350, y=464)

        self.have_an_account_login_label = tk.Label(self, text='Already have an account?', bg='#3C3633', font="Courier 10", foreground='white')
        self.have_an_account_login_label.place(x=95, y=560)

        self.login_clickable = tk.Button(self, text="Log in", fg='#EEEDEB', bg='#3C3633' , bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', command=self.go_to_Login_Page)
        self.login_clickable.place(x=290, y=559)

        self.clear_button = tk.Button(self, text='Clear', width=10, font=('Courier', 15, 'bold'),bg='#d3d3d3', command=self.clear_input)
        self.clear_button.place(x=70, y=510)

        self.sign_up_button = tk.Button(self, text='Continue', width=10, font=('Courier', 15, 'bold'),bg='#d3d3d3', command=self.validate_sign_up)
        self.sign_up_button.place(x=240, y=510)

        self.password_hidden = True 

    def is_valid_gmail(self, email):
        # Check if the email follows a valid format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        
        # Check if the domain is gmail.com
        if email.endswith('@gmail.com'):
            return True
        
        return False

    def show_password(self):
        if self.password_hidden:
            self.password_entry.config(show='')
            self.show_pass.config(bg='#3C3633', fg='white', image=self.eye_hide)
            self.password_hidden = False
        else:
            self.password_entry.config(show='*')
            self.show_pass.config(bg='white', fg='#3C3633', image=self.eye_show)
            self.password_hidden = True

    def confirm_password_show(self):
        if self.password_hidden:
            self.confirm_password_entry.config(show='')
            self.show_confirm_pass.config(bg='#3C3633', fg='white', image=self.eye_hide)
            self.password_hidden = False
        else:
            self.confirm_password_entry.config(show='*')
            self.show_confirm_pass.config(bg='white', fg='#3C3633', image=self.eye_show)
            self.password_hidden = True

    def clear_input(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.gmail_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.Bday_calendar_entry.delete (0, tk.END)
        
    def validate_sign_up(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gmail = self.gmail_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        birthday = self.Bday_calendar_entry.get()
        chosen_date = date.today()
        
        if password != confirm_password:
            messagebox.showerror("Error", "Password and confirm password fields do not match")
            return False
        
        if first_name == '':
            messagebox.showerror('Error', 'First name field is empty, please fill it out.')
            return False
        
        if last_name == '':
            messagebox.showerror('Error', 'Last name field is empty, please fill it out.')
            return False
        
        if gmail == '':
            messagebox.showerror("Error", "Please enter your Gmail Account.")
            return None
        if not self.is_valid_gmail(gmail):
            messagebox.showerror("Error", "Please enter a valid Gmail Account.")
            return None
        
        if username == '':
            messagebox.showerror('Error', 'Username field is empty, please fill it out.')
            return False
        
        if password == '':
            messagebox.showerror('Error', 'Password field is empty, please fill it out.')
            return False
        
        if confirm_password == '':
            messagebox.showerror('Error', 'Confirm password field is empty, please fill it out.')
            return False
        
        if password != confirm_password:
            messagebox.showerror('Error', 'Password and Confirm Password fields do not match.')
            return False
        
        if birthday == '':
            messagebox.showerror('Error', 'Birthday password field is empty, please fill it out.')
            return False
        
        if chosen_date > date.today():
            messagebox.showerror('Error', 'Birth Date is beyond the current date, Please put your real birthday')
            return False
        
        self.go_to_Photo_page()

    def clear_input(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.gmail_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.Bday_calendar_entry.delete(0, tk.END)
        
    def go_to_welcome_page(self):
        self.parent.change_window('Welcome_Page')

    def go_to_Photo_page(self):
        self.parent.change_window('Photo')
        
    def go_to_Login_Page(self):
        self.parent.change_window('Login')
        
    def on_return(self):
        pass


class Photo (tk.Frame):
    def __init__(self, master, signup_frame):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.signup_frame = signup_frame
        self.config(width=400, height=600)
        
        self.Photo_bg = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.Photo_bg.place(x=0, y=0)
        
        #CAPTCHA
        img=self.generate_captha()
        self.pic_frame = tk.Label(self, image=img)
        self.pic_frame.image = img  
        self.pic_frame.place(x=55, y=340)
        
        self.create_refresh_button()
        self.disable_retry_button()
        self.parent.after(INITIAL_DELAY, self.enable_retry_button)

        self.captcha_entry = tk.Entry(self.Photo_bg, border=1, width=20, font=('Courier', 15), fg='white', bg='#59504b')
        self.captcha_entry.place(x=55, y=415)

        self.captcha_window = None
        self.captcha_label_in_window = None
        
        self.Back_button = tk.Button(self, text="Return", bg='#7B6079', bd=0, font=('Courier', 10, 'bold'), foreground='#88f2ea', 
                                     command=self.go_to_create_acc)
        self.Back_button.place(x=5, y=5)
        
        self.Finish_button = CTkButton(self, text='Sign Up', width=300,height=40,corner_radius=30, font=('Courier', 15, 'bold'), bg_color='#3C3633', fg_color='#E0CCBE', 
                                        text_color='black', command=self.signup_button_command)
        self.Finish_button.place(x=60, y=517)

        self.terms_accepted = tk.IntVar()
        self.terms_and_conditions_check_button = tk.Checkbutton(self, text="I accept the Terms and Conditions", variable=self.terms_accepted, 
                                                                command=self.terms_conditions_var)
        self.terms_and_conditions_var = tk.BooleanVar()
        self.terms_and_conditions_check_button.place(x=105, y=480)


        self.image = None
        self.canvas = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.rect = None
        self.crop_history = []

        self.upload_button = tk.Button(self, text="Upload Image", command=self.open_image_window)
        self.upload_button.place(x=150, y=300)

        self.profile_frame = tk.Frame(self, width=200, height=200, bd=2, relief=tk.SOLID)
        self.profile_frame.place(x=100, y=50)
        self.profile_canvas = tk.Canvas(self.profile_frame, width=200, height=200)
        self.profile_canvas.pack(fill=tk.BOTH, expand=1)
        self.profile_label = tk.Label(self.profile_frame, text="Profile Image")
        self.profile_label.pack()
        
        self.image = None 
        self.image_data = None 

    def open_image_window(self):
        self.image_window = tk.Toplevel(self)
        self.image_window.title("Image Window")
        self.image_window.geometry("600x500")
        self.image_window.resizable(False, False)

        self.image_frame = tk.Frame(self.image_window, width=400, height=400, relief=tk.SOLID, bd=2)
        self.image_frame.place(x=10, y=10)

        self.canvas = tk.Canvas(self.image_frame)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.crop_button = tk.Button(self.image_window, text="Crop Image", command=self.start_crop)
        self.crop_button.place(x=450, y=20)

        self.undo_button = tk.Button(self.image_window, text="Undo", command=self.undo_crop)
        self.undo_button.place(x=450, y=60)

        self.redo_button = tk.Button(self.image_window, text="Redo", command=self.redo_crop)
        self.redo_button.place(x=450, y=100)

        self.rotate_button = tk.Button(self.image_window, text="Rotate Image", command=self.rotate_image)
        self.rotate_button.place(x=450, y=140)

        self.done_button = tk.Button(self.image_window, text="Done", command=self.show_profile_image)
        self.done_button.place(x=450, y=180)

        self.upload_button = tk.Button(self.image_window, text="Upload Image", command=self.upload_image)
        self.upload_button.place(x=450, y=210)

        self.exit_button = tk.Button(self.image_window, text="Exit", command=self.close_image_window)
        self.exit_button.place(x=450, y=250)


    def close_image_window(self):
        self.image_window.destroy()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.resize_image()
            self.display_image()
            self.crop_history = []

    def resize_image(self):
        if self.image:
            width_ratio = 400 / self.image.width
            height_ratio = 300 / self.image.height
            scale_factor = min(width_ratio, height_ratio)
            self.image = self.image.resize((int(self.image.width * scale_factor), int(self.image.height * scale_factor)))

    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.canvas.config(width=self.image.width, height=self.image.height)

    def start_crop(self):
        if self.image:
            self.canvas.bind("<Button-1>", self.on_press)
            self.canvas.bind("<B1-Motion>", self.on_drag)
            self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.draw_rectangle()

    def on_release(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.draw_rectangle()
        self.crop_image()

    def draw_rectangle(self):
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, outline="red")

    def crop_image(self):
        if self.image:
            x1 = min(self.start_x, self.end_x)
            y1 = min(self.start_y, self.end_y)
            x2 = max(self.start_x, self.end_x)
            y2 = max(self.start_y, self.end_y)
            cropped_image = self.image.crop((x1, y1, x2, y2))

            width_ratio = self.image_frame.winfo_width() / cropped_image.width
            height_ratio = self.image_frame.winfo_height() / cropped_image.height
            scale_factor = min(width_ratio, height_ratio)

            cropped_image = cropped_image.resize((int(cropped_image.width * scale_factor), int(cropped_image.height * scale_factor)))

            self.crop_history.append(self.image.copy())
            self.image = cropped_image
            self.display_image()

    def undo_crop(self):
        if self.crop_history:
            self.image = self.crop_history.pop()
            self.display_image()

    def redo_crop(self):
        if self.crop_history:
            self.image = self.crop_history.pop()
            self.display_image()

    def rotate_image(self):
        if self.image:
            rotated_image = self.image.rotate(90, expand=True)
            self.image = rotated_image
            self.display_image()

    def show_profile_image(self):
        if self.image:
            profile_image = self.image.copy()
            profile_image.thumbnail((200, 200))

            zoom_factor = min(self.profile_canvas.winfo_width() / profile_image.width,
                              self.profile_canvas.winfo_height() / profile_image.height)

            profile_image = profile_image.resize((int(profile_image.width * zoom_factor),
                                                  int(profile_image.height * zoom_factor)))

            self.profile_photo = ImageTk.PhotoImage(profile_image)

            self.profile_canvas.delete(tk.ALL)

            x_offset = (self.profile_canvas.winfo_width() - profile_image.width) // 2
            y_offset = (self.profile_canvas.winfo_height() - profile_image.height) // 2

            self.profile_canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=self.profile_photo)

            # Convert image to binary data
            self.image_data = self.image_to_binary(profile_image)


    def create_refresh_button(self):
        # Create the refresh button with appropriate callback
        self.refresh_img = Image.open("retry_icon.jpg")
        self.refresh_img = self.refresh_img.resize((25, 25))
        self.refresh_icon = ImageTk.PhotoImage(self.refresh_img)
        self.rfrsh_btn = tk.Button(self, image=self.refresh_icon, highlightbackground='#DE8971', highlightcolor='#DE8971',
                                  border=0, command=self.generate_captcha)
        self.rfrsh_btn.place(x=305, y=414)

    def enable_retry_button(self):
        # Enable the retry button
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
    
    def signup_button_command(self):
        if not self.terms_accepted.get():
            messagebox.showerror("Error", "Please accept the Terms and Conditions.")
            return

        if self.validate_captcha():
            self.go_to_Login_Page()
    
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

    def image_to_binary(self, image):
        with BytesIO() as buffer:
            image.save(buffer, format="PNG")
            return buffer.getvalue()

    def go_to_create_acc(self):
        self.parent.change_window('Signup')
        
        self.generate_captcha()
        
    def go_to_Login_Page(self):
        FName = self.signup_frame.first_name_entry.get().strip()
        LName = self.signup_frame.last_name_entry.get().strip()
        Uname = self.signup_frame.username_entry.get().strip()
        Bday = self.signup_frame.Bday_calendar_entry.get().strip()
        Gmail = self.signup_frame.gmail_entry.get().strip()
        Pass = self.signup_frame.password_entry.get().strip()
        Confirm_Pass = self.signup_frame.confirm_password_entry.get().strip()

        user = Model.User()
        user.firstname = FName
        user.lastname = LName
        user.username = Uname
        user.birthday = Bday
        user.gmail = Gmail
        user.password = Pass
        
        if Pass == Confirm_Pass:
            dbconn = Data_base_Handler.database()
            dbconn.create_sign_up_table(user)

            # Save image data to database
            if self.image_data:
                user.image(self.image_data)
                dbconn.update_user_image(user)

            dbconn.conn.close()
        else:
            messagebox.showerror("Error", "Incorrect Password.")
            return
        
        final = messagebox.askokcancel('Signup', 'Finish signing up?')
        if final:
            self.parent.frames['Signup'].clear_input()
            self.parent.change_window('Login')
    
    
    def on_return(self, **kwargs):
        pass
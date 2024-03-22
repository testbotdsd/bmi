import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import Data_base_Handler
import Model
from customtkinter import *

class BMI(tk.Frame):
    def __init__ (self, master):
        tk.Frame.__init__  (self, master)
        self.parent = master
        self.config(width=400, height=600)
        self.main_frame = tk.Frame(self, bg='#3C3633', height=600, width=450)

        # TOP FRAMES
        self.frame_top_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        self.frame_top_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        
        # BOTTOM FRAMES
        self.frame_bottom_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        self.frame_bottom_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='#747264', relief='flat')
        
        #Result Frame
        self.frame_result = tk.Frame(self.main_frame, bd=10, width=305, height=60, bg='#747264', relief='flat')

        self.main_frame.place(x=0, y=0)
        self.frame_top_left.place(x=45, y=95)
        self.frame_top_right.place(x=215, y=95)
        self.frame_bottom_left.place(x=45, y=190)
        self.frame_bottom_right.place(x=215, y=190)
        self.frame_result.place(x=45, y=332)
        
        # Age Label and Entry
        self.age_label = tk.Label(self.main_frame, text="Age", bg='#747264', font=("Perpetua", 10, 'bold'), foreground='#E0CCBE')
        self.age_label.place(x=120, y=70)
        
        self.age_entry = CTkEntry(self.main_frame, bg_color='#3C3633', corner_radius=15, width=100,
                                  border_color='#3C3633', )
        self.age_entry.place(x=150, y=65)
        
        self.age_entry.bind('<KeyRelease>', self.update_age)

        self.menu_img = Image.open("menu_icon.png")
        self.menu_img = self.menu_img.resize((30, 30))
        self.menu_icon = ImageTk.PhotoImage(self.menu_img)
        self.menu_btn = tk.Button(self, image=self.menu_icon, highlightbackground='#DE8971', highlightcolor='#DE8971',
                                  border=0, command=self.Profile)
        self.menu_btn.place(x=367, y=0)

        self.welcome_label = tk.Label(self, text="BMI Calculator", bg='#3C3633', font=('Courier', 17, 'bold'), 
                                      foreground='#E0CCBE')
        self.welcome_label.place(x=100, y=10)
        
        # WEIGHT LABEL AND ENTRY
        self.weight_kg_label = tk.Label(self.frame_top_left, text="Weight (kg)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.weight_kg_label.place(x=13,y=0)
        self.weight_lb_label = tk.Label(self.frame_top_right, text="Weight (lb)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.weight_lb_label.place(x=14,y=0)

        self.weight_kg_entry = tk.Entry(self.frame_top_left, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.weight_kg_entry.place(x=15, y=30)
        self.weight_lb_entry = tk.Entry(self.frame_top_right, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.weight_lb_entry.place(x=15, y=30)
        
        self.weight_kg_entry.bind('<KeyRelease>', self.update_weight_lb)
        self.weight_lb_entry.bind('<KeyRelease>', self.update_weight_kg)
        

        # HEIGH LABEL AND ENTRY
        self.height_cm_label = tk.Label(self.frame_bottom_left, text="Height (cm)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                        foreground='#E0CCBE')
        self.height_cm_label.place(x=13,y=0)
        self.height_m_label = tk.Label(self.frame_bottom_right, text="Height (m)", bg='#747264', font=("Perpetua", 13, 'bold'), 
                                       foreground='#E0CCBE')
        self.height_m_label.place(x=18,y=0)

        self.height_cm_entry = tk.Entry(self.frame_bottom_left, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.height_cm_entry.place(x=15, y=30)
        self.height_m_entry = tk.Entry(self.frame_bottom_right, width=10, font=("Peroetua", 10), bg='#E0CCBE')
        self.height_m_entry.place(x=15, y=30)

        self.submit_button = tk.Button (self.main_frame, text = 'Calculate BMI', cursor='gumby', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", height=1, width=16, command=self.calculate_BMI)
        self.submit_button.place(x=215, y=285)

        self.clear_button = tk.Button(self.main_frame, text = 'Clear', cursor='gumby', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", width=16, command = self.clear_button)
        self.clear_button.place(x=45, y=285)

        self.history_button = tk.Button (self.main_frame, text = 'View History', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", height=1, width=16, command=self.Show_history)
        self.history_button.place(x=45, y=480)

        self.save_button = tk.Button(self.main_frame, text = 'Save', bg='#E0CCBE', foreground='#3C3633', font=("Perpetua"), 
                                        relief="raised", width=16, command=self.save_info)
        self.save_button.place(x=215, y=480)
        
        # RESULT
        self.result_label = tk.Label (self.frame_result, text='Your BMI is:', bg='#747264', font=("Perpetua", 13, 'bold'), foreground='#E0CCBE')
        self.result_label.place (x =5, y = 6 )
        
        self.result_entry = tk.Entry(self.frame_result, width= 20, font=("Peroetua", 10 ), bg='#E0CCBE')
        self.result_entry.place (x = 120, y = 8)
        
        self.evaluation_result_label = None
        
        self.height_cm_entry.bind('<KeyRelease>', self.update_height_cm)
        self.height_m_entry.bind('<KeyRelease>', self.update_height_m) 
    
  
    def update_weight_lb(self, event):
        try:
            kg_value = float(self.weight_kg_entry.get())
            lb_value = kg_value * 2.20462
            self.weight_lb_entry.delete(0, tk.END)
            self.weight_lb_entry.insert(0, f"{lb_value:.2f}")
        except ValueError:
            self.weight_lb_entry.delete(0, tk.END)
            self.weight_lb_entry.insert(0, "Invalid Input")

    def update_weight_kg(self, event):
        try:
            lb_value = float(self.weight_lb_entry.get())
            kg_value = lb_value / 2.20462
            self.weight_kg_entry.delete(0, tk.END)
            self.weight_kg_entry.insert(0, f"{kg_value:.2f}")
        except ValueError:
            self.weight_kg_entry.delete(0, tk.END)
            self.weight_kg_entry.insert(0, "Invalid Input")

    def update_height_cm(self, event):
        try:
            cm_value = float(self.height_cm_entry.get())
            m_value = cm_value / 100
            self.height_m_entry.delete(0, tk.END)
            self.height_m_entry.insert(0, f"{m_value:.2f}")
        except ValueError:
            self.height_m_entry.delete(0, tk.END)
            self.height_m_entry.insert(0, "Invalid Input")

    def update_height_m(self, event):
        try:
            m_value = float(self.height_m_entry.get())
            cm_value = m_value * 100
            self.height_cm_entry.delete(0, tk.END)
            self.height_cm_entry.insert(0, f"{cm_value:.2f}")
        except ValueError:
            self.height_cm_entry.delete(0, tk.END)
            self.height_cm_entry.insert(0, "Invalid Input")
            
    def update_age(self, event):
        try:
            new_age = self.age_entry.get()
            new_age = ''.join(filter(str.isdigit, new_age))
            new_age = new_age[:2]

            self.age_entry.delete(0, tk.END) 
            self.age_entry.insert(0, new_age)  

        except ValueError:
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, "Invalid Input")
    
    def clear_button(self):
        self.height_cm_entry.delete(0, tk.END)
        self.height_m_entry.delete(0, tk.END)
        self.weight_kg_entry.delete(0, tk.END)
        self.weight_lb_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        self.age_entry.delete(0,tk.END)
        
        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()
            self.evaluation_result_label = None
            
    def calculate_BMI(self):
        try:
            age = self.age_entry.get().strip()

            if not age:
                messagebox.showerror("Error", "Please enter your age.")
                return  

            age = int(age)

            if age < 20:  # For children and teens
                kg_value = float(self.weight_kg_entry.get())
                m_value = float(self.height_m_entry.get())
                bmi_result = kg_value / (m_value ** 2)  
                self.result_entry.delete(0, tk.END)  
                self.result_entry.insert(0, f"{bmi_result:.2f}")

                self.Evaluation_result_for_children_and_teens(bmi_result)

            else:  # For adults
                kg_value = float(self.weight_kg_entry.get())
                m_value = float(self.height_m_entry.get())
                bmi_result = kg_value / (m_value ** 2)  
                self.result_entry.delete(0, tk.END)  
                self.result_entry.insert(0, f"{bmi_result:.2f}")

                self.Evaluation_result_for_adults(bmi_result)

        except ValueError:
            messagebox.showerror("Error", "Invalid input for age, weight, or height.")

    def Evaluation_result_for_children_and_teens(self, bmi_result):
        # BMI categories for children and teens
        if bmi_result < 5:  
            category = 'Very Severely Underweight'
        elif 5 <= bmi_result < 15:  
            category = 'Severely Underweight'
        elif 15 <= bmi_result < 85:  
            category = 'Healthy'
        elif 85 <= bmi_result < 95:  
            category = 'Overweight'
        else:  
            category = 'Obese'

        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()

        self.evaluation_result_label = tk.Label(self.main_frame, text=f'You are {category}', foreground='grey', font=("Poor Richard", 19, 'bold'))
        self.evaluation_result_label.place(x=50, y=420)

    def Evaluation_result_for_adults(self, bmi_result):
        # BMI categories for adults
        if bmi_result < 18.5:
            category = 'Underweight'
        elif bmi_result >= 18.5 and bmi_result < 25:
            category = 'Healthy'
        elif bmi_result >= 25 and bmi_result < 30:
            category = 'Overweight'
        else:
            category = 'Obese'

        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()

        self.evaluation_result_label = tk.Label(self.main_frame, text=f'You are {category}', foreground='grey', font=("Poor Richard", 19, 'bold'))
        self.evaluation_result_label.place(x=50, y=420)

    def go_to_welcome_page(self):
        choice = messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?")
        if choice:
            self.master.change_window('Welcome_Page')
        else:
            pass

    def got_to_profile_page(self):
        self.show_history.destroy()
        self.parent.change_window('Profile')
        
    def save_info(self):
        age = self.age_entry.get().strip()
        kg = self.weight_kg_entry.get().strip()
        lb = self.weight_lb_entry.get().strip()
        cm = self.height_cm_entry.get().strip()
        m = self.height_m_entry.get().strip()

        user_id = self.parent.get_logged_in_user_id()

        save = Model.Save_info()
        save.age = age
        save.kilogram = kg
        save.pounds = lb
        save.centimeter = cm
        save.meter = m


        dbconn = Data_base_Handler.database()
        dbconn.create_save_info_table(save, user_id)
        dbconn.conn.close()
            
    def Show_history(self):    
        self.show_history = tk.Toplevel(self)  
        self.show_history.title("HISTORY") 
        self.show_history.geometry('940x600')
        self.show_history.attributes('-topmost', True) 

        
        title_label = tk.Label(self.show_history, text="BMI HISTORY", font=("TimesNewRoman", 16, "bold"))
        title_label.place(x=430, y=5)

        columns = ("id", "age", "kilogram", "pounds", "centimeter", "meter")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading", background=[('active', '#3484F0')])
        
        self.table = ttk.Treeview(self.show_history, columns=columns, show='headings', height=18)
        self.table.heading("id", text="ID")
        self.table.column("id", width=50)
        self.table.heading("age", text="Age")
        self.table.column("age", width=50)
        self.table.heading("kilogram", text="Weight in Kilogram")
        self.table.column("kilogram", width=200)
        self.table.heading("pounds", text="Weight in Pounds")
        self.table.column("pounds", width=200)
        self.table.heading("centimeter", text="Height in Centimeter")
        self.table.column("centimeter", width=200)
        self.table.heading("meter", text="Height in Meter")
        self.table.column("meter", width=200)
        
        self.table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Adjust this based on your layout
        
        self.delete_button = tk.Button(self.show_history, text="Delete", height=2, width=10, font="TimesNewRoman 10 bold", fg='black', bg='white', relief="flat", command=self.delete_history)
        self.return_button = tk.Button(self.show_history, text="Back", height=2, width=10, fg='black', bg='white', relief="solid", command=self.destroy_top_level)

        self.delete_button.place(x=820, y=530)
        self.return_button.place(x=10, y=530)
        
        self.table.place(x=10, y=40)
        self.updatetable()  

    def updatetable(self):
        self.get_bmi_list()
        self.table.delete(*self.table.get_children())

        for BMI in self.bmi_list:
            row = (BMI.Id, BMI.age, BMI.kilogram, BMI.pounds, BMI.centimeter, BMI.meter)
            self.table.insert('', tk.END, values=row) 
  
    def destroy_top_level(self):
        self.show_history.destroy()
           
    def get_bmi_list(self):
        dbconn=Data_base_Handler.database()
        self.bmi_list=dbconn.get_Bmilist()
        dbconn.conn.close()
    
    def delete_history(self): 
        selections= self.table.selection()

        if len(selections)==0:
            messagebox.showwarning("Warning","select in the table")
            return
        
        proceed=messagebox.askyesno("ask","are you sure you want to delete this user?")

        if not proceed:
            return
        
        for selected_item in selections:
            bmi=self.table.item(selected_item)['values'][0]
            dbconn=Data_base_Handler.database()
            dbconn.delete_Bmi_history(bmi)
            dbconn.conn.close()
            
            self.updatetable()

    def Profile(self):
        self.profile = tk.Toplevel(self)  
        self.profile.title("Profile") 
        self.profile.geometry('400x600')
        self.profile.config(bg='#3C3633')
        self.profile.attributes('-topmost', True)
        
        font_style = ("Garamond", 15, "bold")

        self.profile_label = tk.Label(self.profile, text="PROFILE", bg='#3C3633', font=('Courier', 30, 'bold'), 
                                        foreground='#E0CCBE')
        self.profile_label.place(x=115, y=10)

        self.pic_frame = tk.Frame(self.profile, bd=10, width=150, height=150, bg='#747264', relief='flat')
        self.pic_frame.place(x=45, y=70)

        self.name_label = tk.Label(self.profile, text="Name:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.name_label.place(x=40, y=240)

        self.birthday_label = tk.Label(self.profile, text="Birthday:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.birthday_label.place(x=40, y=300)

        self.gmail_label = tk.Label(self.profile, text="Gmail:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.gmail_label.place(x=40, y=360)

        self.username_label = tk.Label(self.profile, text="Username:", font=('Courier', 13), fg='#EEEDEB', bg='#3C3633')
        self.username_label.place(x=40, y=420)

        self.logout_btn = CTkButton(self.profile, text="Logout", height=50, width=50, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.go_to_main_page)
        self.logout_btn.place(x=151, y=530)
        
        self.return_btn = CTkButton(self.profile, text="Return",width=30,height=30, bg_color="#3C3633", font=font_style, fg_color="#E0CCBE", 
                                   hover_color='#747264', corner_radius=30, text_color='black',command=self.close_top_level)
        self.return_btn.place(x=10, y=10)
        
    def go_to_main_page(self):
        self.profile.destroy()
        self.parent.change_window('Welcome_Page')
        
    def close_top_level(self):
        self.profile.destroy()
        
    def on_return(self):
        pass


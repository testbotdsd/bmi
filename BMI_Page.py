import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import Data_base_Handler
import Model

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
        self.age_label.place(x=45, y=70)
        
        self.age_entry = tk.Entry(self.main_frame, width=39, font=("Perpetua", 10), bg='#E0CCBE',)
        self.age_entry.place(x=78, y=70)
        
        self.age_entry.bind('<KeyRelease>', self.update_age)

        self.menu_img = Image.open("menu_icon.png")
        self.menu_img = self.menu_img.resize((30, 30))
        self.menu_icon = ImageTk.PhotoImage(self.menu_img)
        self.menu_btn = tk.Button(self, image=self.menu_icon, highlightbackground='#DE8971', highlightcolor='#DE8971',
                                  border=0, command=self.got_to_profile_page)
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
                                        relief="raised", height=1, width=16, command=self.go_to_history_info)
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
            
    def go_to_history_info(self):
        self.parent.change_window('History')

        
    def on_return(self):
        pass
            
class Show_history(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.config(width=400, height=600)
        self.main_frame = tk.Frame(self, bg='#3C3633', height=600, width=450)
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Adjust this based on your layout
        
        title_label = tk.Label(self.main_frame, text="BMI HISTORY", font=("TimesNewRoman", 16, "bold"), bg="orange")
        title_label.place(x=50, y=10)

        columns = ("id", "age", "kilogram", "pounds", "centimeter", "meter")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background='#e5e5e5', foreground='black', fieldbackground='#e5e5e5')
        style.configure("Treeview.Heading", background='#e5e5e5', foreground='black')
        style.map("Treeview", background=[('selected', "#14213d")])
        
        self.table = ttk.Treeview(self.main_frame, columns=columns, show='headings', height=25)
        self.table.heading("id", text="ID")
        self.table.column("id", width=50)
        self.table.heading("age", text="Age")
        self.table.column("age", width=50)
        self.table.heading("kilogram", text="Kilogram")
        self.table.column("kilogram", width=200)
        self.table.heading("pounds", text="Pounds")
        self.table.column("pounds", width=200)
        self.table.heading("centimeter", text="Centimeter")
        self.table.column("centimeter", width=200)
        self.table.heading("meter", text="Meter")
        self.table.column("meter", width=200)
        
        self.table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Adjust this based on your layout
        
        self.add_button = tk.Button(self.main_frame, text="Add", height=2, width=10, font="TimesNewRoman 10 bold", fg='black', bg='white', relief="flat")
        self.delete_button = tk.Button(self.main_frame, text="Delete", height=2, width=10, font="TimesNewRoman 10 bold", fg='black', bg='white', relief="flat")
        self.update_button = tk.Button(self.main_frame, text="Update", height=2, width=10, font="TimesNewRoman 10 bold", fg='black', bg='white', relief="flat")
        self.return_button = tk.Button(self.main_frame, text="🢀", height=2, width=10, fg='black', bg='white', relief="solid", command=self.go_to_Bmi_page)

        self.add_button.place(x=5, y=350)
        self.delete_button.place(x=100, y=350)
        self.update_button.place(x=150, y=350)
        self.return_button.place(x=5, y=5)
        
        self.table.place(x=10, y=40)
        self.updatetable()
    
    def updatetable(self):
        self.get_bmi_list()
        self.table.delete(*self.table.get_children())

        for BMI in self.bmi_list:
           row = (BMI.Id,BMI.age,BMI.kilogram,BMI.pounds,BMI.centimeter,BMI.meter)
           self.table.insert('', tk.END, values=row) 
           
    def go_to_Bmi_page(self):
        self.parent.change_window('BMI')
           
    def get_bmi_list(self):
        dbconn=Data_base_Handler.database()
        self.bmi_list=dbconn.get_Bmilist()
        dbconn.conn.close()
    
    def on_return(self):
        pass



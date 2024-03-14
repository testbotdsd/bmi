import tkinter as tk

class BMI(tk.Frame):
    def __init__ (self, master):
        tk.Frame.__init__  (self, master)
        self.parent = master
        self.config(width=400, height=600)
        
        # MAIN FRAME
        self.main_frame = tk.Frame(self, bd=20, width=350, height=600, bg='sky blue', relief='sunken')
        self.welcome_frame = tk.Frame(self.main_frame, bd=10, width=300, height=70, bg='grey', relief='raised')
        
        # TOP FRAMES
        self.frame_top_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='grey', relief='raised')
        self.frame_top_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='grey', relief='raised')
        
        # BOTTOM FRAMES
        self.frame_bottom_left = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='grey', relief='raised')
        self.frame_bottom_right = tk.Frame(self.main_frame, bd=10, width=140, height=80, bg='grey', relief='raised')
        
        #Result Frame
        self.frame_result = tk.Frame(self.main_frame, bd=10, width=300, height=70, bg='grey', relief='raised')

        self.main_frame.place(x=0, y=0)
        self.welcome_frame.place(x=10, y=10)
        self.frame_top_left.place(x=10, y=95)
        self.frame_top_right.place(x=168, y=95)
        self.frame_bottom_left.place(x=10, y=190)
        self.frame_bottom_right.place(x=168, y=190)
        self.frame_result.place(x=8, y=400)

        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to BMI Calculator", bg='grey', font=("Poor Richard", 16, 'bold'), foreground='white')
        self.welcome_label.place(x=7, y=10)

        self.submit_button = tk.Button (self.main_frame, text = 'Calculate BMI', cursor='gumby', bg="grey", fg="white", font=("SimSun"), relief="raised", height=1, width=15, command=self.calculate_BMI)
        self.submit_button.place(x=172, y=285)

        self.clear_button = tk.Button(self.main_frame, text = 'CLEAR', cursor='gumby', bg="grey", fg="white", font=("SimSun"), relief="raised", width=16, command = self.clear_button)
        self.clear_button.place(x=10, y=285)

        # WEIGHT LABEL AND ENTRY
        self.weight_kg_label = tk.Label(self.frame_top_left, text="Weight (kg)", bg='grey', font=("Perpetua", 13, 'bold'), foreground='white')
        self.weight_kg_label.place(x=13,y=0)
        self.weight_lb_label = tk.Label(self.frame_top_right, text="Weight (lb)", bg='grey', font=("Perpetua", 13, 'bold'), foreground='white')
        self.weight_lb_label.place(x=14,y=0)

        self.weight_kg_entry = tk.Entry(self.frame_top_left, width=10, font=("Peroetua", 10))
        self.weight_kg_entry.place(x=15, y=30)
        self.weight_lb_entry = tk.Entry(self.frame_top_right, width=10, font=("Peroetua", 10))
        self.weight_lb_entry.place(x=15, y=30)
        
        self.weight_kg_entry.bind('<KeyRelease>', self.update_weight_lb)
        self.weight_lb_entry.bind('<KeyRelease>', self.update_weight_kg)
        

        # HEIGH LABEL AND ENTRY
        self.height_cm_label = tk.Label(self.frame_bottom_left, text="Height (cm)", bg='grey', font=("Perpetua", 13, 'bold'), foreground='white')
        self.height_cm_label.place(x=13,y=0)
        self.height_m_label = tk.Label(self.frame_bottom_right, text="Height (m)", bg='grey', font=("Perpetua", 13, 'bold'), foreground='white')
        self.height_m_label.place(x=18,y=0)

        self.height_cm_entry = tk.Entry(self.frame_bottom_left, width=10, font=("Peroetua", 10))
        self.height_cm_entry.place(x=15, y=30)
        self.height_m_entry = tk.Entry(self.frame_bottom_right, width=10, font=("Peroetua", 10))
        self.height_m_entry.place(x=15, y=30)
        
        # RESULT
        self.result_label = tk.Label (self.frame_result, text='Your BMI is:',  bg='grey', font=("Perpetua", 13, 'bold'), foreground='white')
        self.result_label.place (x =5, y = 6 )
        
        self.result_entry = tk.Entry(self.frame_result, width= 20, font=("Peroetua", 10 ))
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
    
    def clear_button(self):
        self.height_cm_entry.delete(0, tk.END)
        self.height_m_entry.delete(0, tk.END)
        self.weight_kg_entry.delete(0, tk.END)
        self.weight_lb_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
        
        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()
            self.evaluation_result_label = None
            
    def calculate_BMI(self):
        try:
            kg_value = float(self.weight_kg_entry.get())
            m_value = float(self.height_m_entry.get())
            bmi_result = kg_value / (m_value ** 2)  
            self.result_entry.delete(0, tk.END)  
            self.result_entry.insert(0, f"{bmi_result:.2f}")
            
            self.Evaluation_result(bmi_result)
            
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Invalid Input")
            
    def Evaluation_result(self, bmi_result):
        if bmi_result < 18.5:
            category = 'Underweight'
        elif bmi_result <= 24.9:
            category = 'Healthy'
        elif bmi_result <= 29.9:
            category = 'Overweight'
        elif bmi_result <= 34.9:
            category = 'Obese'
        else:
            category = 'Extremely Obese'

        if self.evaluation_result_label:
            self.evaluation_result_label.destroy()

        self.evaluation_result_label = tk.Label(self.main_frame, text=f'You are {category}', foreground='grey', font=("Poor Richard", 19, 'bold'))
        self.evaluation_result_label.place(x=50, y=500)
        
    def on_return(self):
        pass

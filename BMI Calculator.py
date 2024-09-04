import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
from tkinter import PhotoImage

class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('BODY MASS INDEX(BMI) CALCULATOR')

        font1 = ('Arial', 40, 'bold')
        font2 = ('Arial', 18)
        
        self.image_path= PhotoImage(file=r'C:\Users\HP\OneDrive\Pictures\Saved Pictures\body-mass-index-calculator.png')
        self.bg_image=tk.Label(master, image=self.image_path)
        self.bg_image.pack()

        self.title_label = tk.Label(master, text='BMI CALCULATOR', font=font1)
        self.title_label.place(x=125, y=20)
        
        self.weight_label = tk.Label(master, bg='red', text='Enter the WEIGHT in Kilograms(kg):', font=font2)
        self.weight_label.place(x=167, y=80)
        self.weight_entry = tk.Entry(master, bg='yellow', font=font2)
        self.weight_entry.place(x=230, y=110)

        self.height_label = tk.Label(master, bg='red', text='Enter the HEIGHT in meters(m):', font=font2)
        self.height_label.place(x=167, y=150)
        self.height_entry = tk.Entry(master, bg='yellow', font=font2)
        self.height_entry.place(x=230, y=180)

        def clicked():
            self.calculate_button['state'] = 'disabled'
            self.calculate_button['text'] = 'BMI'
            self.calculate_button['bg'] = 'white'
            self.calculate_label = tk.Label(master, text='bmi')
            self.calculate_label.place()  

        self.calculate_button = tk.Button(master, text="CALCULATE", command=self.calculate_bmi, font=font2, fg='white', bg='red')
        self.calculate_button.place(x=280, y=250)

        self.result_label = tk.Label(master, text="", font=font2)
        self.result_label.place(x=240, y=315)

        self.history_button = tk.Button(master, text="VIEW HISTORY", command=self.show_history, font=font2)
        self.history_button.place(x=265, y=400)

        self.data_file = "bmi_data.txt"
        self.data = self.load_data()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            bmi = weight / (height**2)
            category = self.get_category(bmi)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
            self.save_data(weight, height, bmi, category)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def get_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def load_data(self):
        data = []
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                for line in f:
                    entry = line.strip().split(",")
                    data.append(entry)
        return data

    def save_data(self, weight, height, bmi, category):
        with open(self.data_file, "a") as f:
            f.write(f"{weight},{height},{bmi},{category}\n")

    def show_history(self):
        if self.data:
            weights = [float(entry[0]) for entry in self.data]
            bmis = [float(entry[2]) for entry in self.data]

            plt.plot(weights, bmis, 'o-')
            plt.xlabel('Weight (kg)')
            plt.ylabel('BMI')
            plt.title('BMI History')
            plt.grid(True)
            plt.show()
        else:
            messagebox.showinfo("Info", "No history data available.")

def main():
    root = tk.Tk()
    root.geometry('700x500')
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
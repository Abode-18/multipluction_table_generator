# the project is a program that write the result of the numbers between the 2 numbers that the user enters multiplayed by the numbers 1-10
#2/8/2025 by: Abdulrahman alowidi and the help of mohamad

import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import sys
import os

# an edit to make sure that the exe file would work
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller exe"""
    try:
        base_path = sys._MEIPASS  # مكان الملفات داخل exe
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)




#the process(function)
def multiplaying_table():
    
    #checking input number 1:a
    a = entry_start.get()
    if a == "":
        messagebox.showerror("Error", "enter a vailed number")
        return
    elif a.isdigit():
        a = int(a)
    else:
        messagebox.showerror("Error", "enter a vailed number")
        return

    #checking input number 2: b
    b = entry_end.get()
    if b == "":
        messagebox.showerror("Error", "enter a vailed number")
        return
    elif b.isdigit():
        b = int(b)
    else:
        messagebox.showerror("Error", "enter a vailed number")
        return

    # checking that the ending number is more than the starting number
    if b < a:
        messagebox.showerror("Error", "the ending number must be more than the starting number")
        return

    #the multiplaying process
    output_text.delete("1.0", tk.END)  # English: clear previous output
    for x in range(a, b + 1):
        for y in range(1, 11):
            r = x * y
            output_text.insert(tk.END, f"{x} × {y} = {r}\n")  # English: insert result into text area
        output_text.insert(tk.END, "\n")  # English: add empty line between numbers

# GUI setup
root = tk.Tk()
root.title("Multiplication_Table _Generator")
root.geometry("1200x1920")  # English: set window size
root.configure(bg="#FFD700")  # English: set background color

# Load logo with Pillow
try:
    image = Image.open(resource_path("school logo.png"))  # يمكن PNG أو JPG
    image = image.resize((50,50))  # English: resize logo to fit GUI
    logo_img = ImageTk.PhotoImage(image)
    logo_label = tk.Label(root, image=logo_img, bg="#FFD700")
    logo_label.pack(pady=10)
except Exception as e:
    logo_label = tk.Label(root, text="[شعار المدرسة]", font=("Arial", 20), bg="#FFD700", fg="#00008B")
    logo_label.pack(pady=10)
    print("Error loading logo:", e)


# School name after logo
school_label_top = tk.Label(root, text="talanted tech high school in Jeddah", font=("Arial", 26, "bold"), bg="#FFD700", fg="#8B0000")
school_label_top.pack(pady=10)  # English: school name displayed after logo

# Title label
title_label = tk.Label(root, text="Multiplication_Table _Generator", font=("Arial", 30, "bold"), bg="#FFD700", fg="#8B0000")
title_label.pack(pady=20)  # English: add top padding

# Input frame
frame_inputs = tk.Frame(root, bg="#FFD700")
frame_inputs.pack(pady=20)

label_start = tk.Label(frame_inputs, text="Starting num", font=("Arial", 18), bg="#FFD700", fg="#00008B")
label_start.grid(row=0, column=0, padx=20, pady=10, sticky="e")
entry_start = tk.Entry(frame_inputs, font=("Arial", 24), width=10)
entry_start.grid(row=0, column=1, padx=20, pady=10)

label_end = tk.Label(frame_inputs, text="Ending num", font=("Arial", 18), bg="#FFD700", fg="#00008B")
label_end.grid(row=1, column=0, padx=20, pady=10, sticky="e")
entry_end = tk.Entry(frame_inputs, font=("Arial", 24), width=10)
entry_end.grid(row=1, column=1, padx=20, pady=10)

# Run button
run_button = tk.Button(root, text="show multipluction table", font=("Arial", 18, "bold"), bg="#32CD32", fg="white", command=multiplaying_table)
run_button.pack(pady=5)  # English: add padding below the button

# Output text area with scrollbar
output_text = scrolledtext.ScrolledText(root, width=50, height=10, font=("Arial", 18), bg="#FFFACD", fg="#000000")
output_text.pack(pady=20)  # English: add padding around text area

# Student credit
student_label = tk.Label(root, text="a project for the student: Abdulrahman Alowidi", font=("Arial", 18, "italic"), bg="#FFD700", fg="#00008B")
student_label.pack(pady=10)  # English: show student credit below output

root.mainloop()  # English: run the main GUI loop

import tkinter as tk
from tkinter import ttk, messagebox

# ---- Functions ----

def add_student():
    name = name_var.get()
    roll = roll_var.get()
    marks = marks_var.get()
    if name and roll and marks:
        with open("students.txt", "a") as f:
            f.write(f"{name},{roll},{marks}\n")
        messagebox.showinfo("Success", "Student added successfully!")
        name_var.set("")
        roll_var.set("")
        marks_var.set("")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def view_students():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            if lines:
                result = ""
                for line in lines:
                    name, roll, marks = line.strip().split(",")
                    result += f"Name: {name}, Roll: {roll}, Marks: {marks},\n"
                messagebox.showinfo("Student Records", result)
            else:
                messagebox.showinfo("Records", "No records found.")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No student records file found.")

def search_student():
    roll = search_var.get()
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, r, marks = line.strip().split(",")
                if r == roll:
                    messagebox.showinfo("Found", f"Name: {name}, Roll: {r}, Marks: {marks}")
                    found = True
                    break
        if not found:
            messagebox.showinfo("Not Found", "Student not found.")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No student records file found.")

# ---- UI Setup ----

root = tk.Tk()
root.title("📚 Student Record Manager")
root.geometry("400x400")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11), background="#f0f4f7")
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TEntry", padding=4)

name_var = tk.StringVar()
roll_var = tk.StringVar()
marks_var = tk.StringVar()
search_var = tk.StringVar()

ttk.Label(root, text="Enter Student Details", font=("Segoe UI", 13, "bold")).pack(pady=10)

ttk.Label(root, text="Name:").pack(pady=(5, 0))
ttk.Entry(root, textvariable=name_var, width=30).pack()

ttk.Label(root, text="Roll Number:").pack(pady=(5, 0))
ttk.Entry(root, textvariable=roll_var, width=30).pack()

ttk.Label(root, text="Marks:").pack(pady=(5, 0))
ttk.Entry(root, textvariable=marks_var, width=30).pack()

ttk.Button(root, text="➕ Add Student", command=add_student).pack(pady=10)
ttk.Button(root, text="📖 View All Students", command=view_students).pack(pady=5)

ttk.Separator(root, orient="horizontal").pack(fill="x", pady=15)

ttk.Label(root, text="Search by Roll Number", font=("Segoe UI", 11, "bold")).pack()
ttk.Entry(root, textvariable=search_var, width=30).pack()
ttk.Button(root, text="🔍 Search", command=search_student).pack(pady=10)

root.mainloop()

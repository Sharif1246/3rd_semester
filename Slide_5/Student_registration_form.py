# This is lab 2
import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x350")
root.minsize(400, 300)

tk.Label(root, text="Student Registration Form", font=("Arial", 20)).grid(
    row=0, column=0, columnspan=2, pady=20
)

tk.Label(root, text="Student ID:").grid(row=1, column=0, sticky="w", padx=20, pady=10)
student_id = tk.Entry(root)
student_id.grid(row=1, column=1, padx=20, pady=10)

tk.Label(root, text="Name:").grid(row=2, column=0, sticky="w", padx=20, pady=10)
name = tk.Entry(root)
name.grid(row=2, column=1, padx=20, pady=10)

tk.Label(root, text="Department:").grid(row=3, column=0, sticky="w", padx=20, pady=10)
department = tk.Entry(root)
department.grid(row=3, column=1, padx=20, pady=10)

tk.Label(root, text="Semester:").grid(row=4, column=0, sticky="w", padx=20, pady=10)
semester = tk.Entry(root)
semester.grid(row=4, column=1, padx=20, pady=10)

def save():
    print("Student ID:", student_id.get())
    print("Name:", name.get())
    print("Department:", department.get())
    print("Semester:", semester.get())

def clear():
    student_id.delete(0, tk.END)
    name.delete(0, tk.END)
    department.delete(0, tk.END)
    semester.delete(0, tk.END)

tk.Button(root, text="Save", command=save).grid(
    row=5, column=0, padx=20, pady=20
)

tk.Button(root, text="Clear", command=clear).grid(
    row=5, column=1, padx=20, pady=20
)

root.mainloop()
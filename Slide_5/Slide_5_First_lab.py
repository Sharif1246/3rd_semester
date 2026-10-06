 # This is the first tkinter window

import tkinter as tk

root = tk.Tk()
root.title("Advanced Programming Lab")
root.geometry("500x300")
root.minsize(400, 250)

heading = tk.Label(root, text="Advanced Programming Lab", font=("Arial", 20))
heading.pack(pady=20)

button1 = tk.Button(root, text="Button 1")
button1.pack(fill="x", padx=40, pady=5)

button2 = tk.Button(root, text="Button 2")
button2.pack(fill="x", padx=40, pady=5)

button3 = tk.Button(root, text="Button 3")
button3.pack(padx=40, pady=5)

root.mainloop()
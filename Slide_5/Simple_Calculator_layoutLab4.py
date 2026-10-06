import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.minsize(300, 400)

display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

for column in range(4):
    root.columnconfigure(column, weight=1)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    ("C", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3)
]

for text, row, column in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    root.rowconfigure(row, weight=1)

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("Responsive Layout")
root.geometry("600x400")
root.minsize(400, 300)

header = tk.Frame(root)
header.pack(fill="x", padx=10, pady=10)

tk.Label(header, text="Advanced Programming", font=("Arial", 20)).pack()

content = tk.Frame(root)
content.pack(fill="both", expand=True, padx=10, pady=10)

content.columnconfigure(1, weight=1)

tk.Label(content, text="Student Name:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

name_entry = tk.Entry(content)
name_entry.grid(
    row=0, column=1, padx=10, pady=10, sticky="ew"
)

tk.Label(content, text="Student ID:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)

id_entry = tk.Entry(content)
id_entry.grid(
    row=1, column=1, padx=10, pady=10, sticky="ew"
)

footer = tk.Frame(root)
footer.pack(fill="x", padx=10, pady=10)

tk.Label(footer, text="CS.SE.0317 • Advanced Programming").pack()

root.mainloop()
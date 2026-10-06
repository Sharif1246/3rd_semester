import tkinter as tk


class PersonalInformationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Information Form")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)

        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(fill="x", padx=20, pady=20)

        self.header_label = tk.Label(
            self.header_frame,
            text="Personal Information Form",
            font=("Arial", 22)
        )
        self.header_label.pack()

        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        self.form_frame.columnconfigure(1, weight=1)

        self.full_name = tk.Entry(self.form_frame)
        self.student_id = tk.Entry(self.form_frame)
        self.email = tk.Entry(self.form_frame)
        self.department = tk.Entry(self.form_frame)
        self.semester = tk.Entry(self.form_frame)
        self.phone = tk.Entry(self.form_frame)

        fields = [
            ("Full Name:", self.full_name),
            ("Student ID:", self.student_id),
            ("Email:", self.email),
            ("Department:", self.department),
            ("Semester:", self.semester),
            ("Phone:", self.phone)
        ]

        for row, (label_text, entry) in enumerate(fields):
            tk.Label(
                self.form_frame,
                text=label_text,
                font=("Arial", 12)
            ).grid(
                row=row,
                column=0,
                sticky="w",
                padx=10,
                pady=10
            )

            entry.grid(
                row=row,
                column=1,
                sticky="ew",
                padx=10,
                pady=10
            )

        self.footer_frame = tk.Frame(self.root)
        self.footer_frame.pack(fill="x", padx=30, pady=20)

        tk.Button(
            self.footer_frame,
            text="Save",
            width=12,
            command=self.save_information
        ).pack(side="left", padx=10)

        tk.Button(
            self.footer_frame,
            text="Clear",
            width=12,
            command=self.clear_information
        ).pack(side="left", padx=10)

        tk.Button(
            self.footer_frame,
            text="Exit",
            width=12,
            command=self.root.destroy
        ).pack(side="right", padx=10)

    def save_information(self):
        print("Personal Information")
        print("Full Name:", self.full_name.get())
        print("Student ID:", self.student_id.get())
        print("Email:", self.email.get())
        print("Department:", self.department.get())
        print("Semester:", self.semester.get())
        print("Phone:", self.phone.get())
        print("-" * 30)

    def clear_information(self):
        self.full_name.delete(0, tk.END)
        self.student_id.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.department.delete(0, tk.END)
        self.semester.delete(0, tk.END)
        self.phone.delete(0, tk.END)


root = tk.Tk()
app = PersonalInformationForm(root)
root.mainloop()
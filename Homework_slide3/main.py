
import json
from pathlib import Path
import shutil

DATA_FILE = Path("students.json")
BACKUP_FILE = Path("students_backup.json")


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid data format.")
            return []

        return data

    except (json.JSONDecodeError, OSError):
        print("Could not read students.json.")
        return []


def save_students(students):
    try:
        if DATA_FILE.exists():
            shutil.copy2(DATA_FILE, BACKUP_FILE)

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError:
        print("Could not save student data.")
        return False


def validate_student_id(student_id):
    return student_id.isdigit() and len(student_id) >= 3


def validate_required_fields(student_id, name, department, semester):
    if not student_id or not name or not department or not semester:
        return False

    if not validate_student_id(student_id):
        return False

    return True


def add_student():
    students = load_students()

    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    department = input("Enter department: ").strip()
    semester = input("Enter semester: ").strip()

    if not validate_required_fields(student_id, name, department, semester):
        print("Invalid input. All fields are required and ID must contain at least 3 digits.")
        return

    if any(student["student_id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    students.append({
        "student_id": student_id,
        "name": name,
        "department": department,
        "semester": semester
    })

    if save_students(students):
        print("Student added successfully.")


def list_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\nStudent List")
    print("-" * 60)

    for student in students:
        print(
            f"ID: {student['student_id']} | "
            f"Name: {student['name']} | "
            f"Department: {student['department']} | "
            f"Semester: {student['semester']}"
        )


def search_student():
    students = load_students()

    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found")
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Department: {student['department']}")
            print(f"Semester: {student['semester']}")
            return

    print("Student not found.")


def update_student():
    students = load_students()

    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student["student_id"] == student_id:
            name = input("Enter new name: ").strip()
            department = input("Enter new department: ").strip()
            semester = input("Enter new semester: ").strip()

            if not name or not department or not semester:
                print("All fields are required.")
                return

            student["name"] = name
            student["department"] = department
            student["semester"] = semester

            if save_students(students):
                print("Student updated successfully.")

            return

    print("Student not found.")


def delete_student():
    students = load_students()

    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["student_id"] == student_id:
            confirmation = input(
                f"Delete {student['name']}? (yes/no): "
            ).strip().lower()

            if confirmation != "yes":
                print("Delete cancelled.")
                return

            students.remove(student)

            if save_students(students):
                print("Student deleted successfully.")

            return

    print("Student not found.")


def display_menu():
    print("\nStudent Management System")
    print("=" * 30)
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


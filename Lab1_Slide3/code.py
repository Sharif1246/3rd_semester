filename = "students.txt"

try:
    with open(filename, "r") as file:
        records = file.readlines()

    print("All Students:")
    for record in records:
        print(record.strip())

    student_id = input("\nEnter student ID to search: ")

    found = False

    for record in records:
        if record.startswith(student_id + ","):
            print("Student found:", record.strip())
            found = True
            break

    if not found:
        print("Student not found.")

    with open(filename, "a") as file:
        file.write("106,Farid,Computer Science\n")

    with open(filename, "r") as file:
        total_records = sum(1 for _ in file)

    print("Total records:", total_records)

except FileNotFoundError:
    print("students.txt does not exist.")
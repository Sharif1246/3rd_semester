import csv
import os

input_file = os.path.join(os.path.dirname(__file__), "students.csv")
output_file = os.path.join(os.path.dirname(__file__), "results.csv")
threshold = 60

with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    students = []

    for row in reader:
        midterm = float(row["midterm"])
        final = float(row["final"])

        total = midterm + final
        average = total / 2

        students.append({
            "student_id": row["student_id"],
            "name": row["name"],
            "midterm": midterm,
            "final": final,
            "total": total,
            "average": average
        })

print("Students who passed:")

for student in students:
    if student["average"] >= threshold:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"Average: {student['average']:.2f}"
        )

with open(output_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "student_id",
        "name",
        "midterm",
        "final",
        "total",
        "average"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print()
print(f"Results saved to {output_file}")
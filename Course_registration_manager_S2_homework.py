from typing import TypeVar

T = TypeVar("T")


def first_item(items: list[T]) -> T:
    return items[0]


students: dict[int, dict[str, object]] = {}


def add_student(student_id: int, name: str) -> None:
    if student_id in students:
        print("Student already exists.")
        return

    students[student_id] = {
        "name": name,
        "courses": set()
    }

    print("Student added successfully.")


def register_course(student_id: int, course: str) -> None:
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]
    courses.add(course)
    print("Course registered successfully.")


def drop_course(student_id: int, course: str) -> None:
    if student_id not in students:
        print("Student not found.")
        return

    courses = students[student_id]["courses"]

    if course not in courses:
        print("Course not registered.")
        return

    courses.remove(course)
    print("Course dropped successfully.")


def search_student(student_id: int) -> None:
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Courses: {sorted(student['courses'])}")


def display_all_unique_courses() -> None:
    all_courses = {
        course
        for student in students.values()
        for course in student["courses"]
    }

    print("All unique registered courses:")

    for course in sorted(all_courses):
        print(course)


def find_students_by_course(course: str) -> list[str]:
    return [
        student["name"]
        for student in students.values()
        if course in student["courses"]
    ]


def display_students_by_name() -> None:
    sorted_students = sorted(
        students.items(),
        key=lambda item: item[1]["name"]
    )

    print("Students sorted by name:")

    for student_id, student in sorted_students:
        print(f"{student['name']} - ID: {student_id}")


def main() -> None:
    add_student(101, "Ahmad")
    add_student(102, "Ali")
    add_student(103, "Omar")
    add_student(104, "Zahra")

    print()

    register_course(101, "Python")
    register_course(101, "Database")
    register_course(102, "Python")
    register_course(102, "Networks")
    register_course(103, "Database")
    register_course(103, "Python")
    register_course(104, "Networks")
    register_course(104, "Artificial Intelligence")

    print()

    print("Student search:")
    search_student(101)

    print()

    drop_course(101, "Database")

    print()

    print("Student after dropping Database:")
    search_student(101)

    print()

    display_all_unique_courses()

    print()

    course = "Python"
    students_in_course = find_students_by_course(course)

    print(f"Students registered for {course}:")
    for name in students_in_course:
        print(name)

    print()

    display_students_by_name()

    print()

    numbers = [10, 20, 30]
    print(f"Generic helper result: {first_item(numbers)}")


if __name__ == "__main__":
    main()
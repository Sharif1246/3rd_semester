

from typing import TypedDict


class StudentRecord(TypedDict):
    name: str
    courses: set[str]


students: dict[str, StudentRecord] = {}


def add_student(student_id: str, student_name: str) -> None:
    students[student_id] = {
        "name": student_name,
        "courses": set()
    }


def add_course(student_id: str, course_name: str) -> None:
    if student_id in students:
        students[student_id]["courses"].add(course_name)


def drop_course(student_id: str, course_name: str) -> None:
    if student_id in students:
        students[student_id]["courses"].discard(course_name)


def common_courses(student_id1: str, student_id2: str) -> set[str]:
    if student_id1 in students and student_id2 in students:
        return students[student_id1]["courses"] & students[student_id2]["courses"]

    return set()


def all_courses() -> set[str]:
    courses: set[str] = set()

    for student in students.values():
        courses = courses | student["courses"]

    return courses


add_student("01", "Ahmad")
add_student("02", "Ali")

add_course("01", "Math")
add_course("01", "Physics")

add_course("02", "Math")
add_course("02", "Chemistry")
add_course("02", "Math")

print(students)
print(common_courses("01", "02"))
print(all_courses())

drop_course("01", "Math")

print(students)
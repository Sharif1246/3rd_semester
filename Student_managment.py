# Week 3 lab

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name,email):
        self.name = name
        self.email = email

    @abstractmethod
    def role_info(self):
        pass
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email address must have an '@' character")
        self._email = value
    def __str__(self):
        return self.name + " " + self.email

class Student(Person):

    def role_info(self):
        return "I am a student"

    def __str__(self):
        return self.name + " " + self.email

class Teacher(Person):


    def role_info(self):
        return "I am a teacher"


class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def __str__(self):
        students_info = ", ".join(str(student) for student in self.students)
        return self.course_name + " " + students_info


teacher = Teacher("Ahmad","ahmad@gmail.com")

student = Student("karim","karim@gmail.com")

obj = [teacher,student]
for i in obj:
    print(i.role_info())
    print(i)

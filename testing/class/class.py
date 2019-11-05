import datetime

from typing import List

class Person():
    def __init__(self, first_name: str, last_name: str, email: str, DOB: datetime):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = None
        self.__DOB = datetime

    def greet(self) -> str:
        pass

    def get_age(self) ->  int:
        pass


class Teacher(Person):
    def __init__(self, OCT_PIN: int, school: str, email_k12: str, classes: List[Class_]):
        self.OCT_PIN = OCT_PIN
        self.school = school
        self.email_k12 = email_k12
        self.classes = None
    
    def assign_work(self, Class_):
        pass

    def greet(self):
        pass

    def add_class(self, Class_):
        pass

    def remove_class(self, Class_):
        pass


class Class_():
    def __init__(self, subject_name: str, students:  List[Student]):
        self.subject_name = subject_name
        self.students = students
    
    def add_student(self, Student):
        pass

    def remove_student(self, Student):
        pass


class Student(Person):
    def __init__(self, email_k12: str,  student_number: int):
        self.email_k12 = email_k12
        self.student_number = student_number

    def greet():
        pass
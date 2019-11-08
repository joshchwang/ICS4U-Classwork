import datetime

from typing import List


class Person():
    def __init__(self, first_name: str, last_name: str, DOB: datetime, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email


    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name}."

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return f"{self._first_name}"

    def set_last_name(self, last_name):
        self._last_name  = last_name
    
    def get_last_name(self):
        return f"{self._last_name}"

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return f"{self._email}"

    def set_DOB(self, DOB):
        raise AttributeError
    
    def get_DOB(self):
        return self._DOB

    def get_age(self) ->  int:
        return datetime.datetime.now().year - self._DOB.year


class Student(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime, student_number: int):
        super().__init__(first_name, last_name, DOB)
        self._email_k12 = f"{self._first_name.lower()}.{self._last_name.lower()}{(self._DOB.year % 100) + 18}@ycdsbk12.ca"
        self._student_number = student_number

    def set_student_number(self, student_number):
        if type(student_number) == int:
            self._student_number = student_number
        else:
            raise TypeError
    
    def get_student_number(self):
        return self._student_number

    def greet(self):
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a student."


class Classroom():
    warnings = []

    def __init__(self, name: str):
        self._name = name
        self._students = []

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_students(self, students):
        self._students = students

    def get_students(self):
        return self._students
    
    def add_student(self, Student):
        if Student not in self._students:
            self._students.append(Student)
        else:
            raise Exception

        if len(self._students) > 33:
            Classroom.warnings.append(f"{self._name} has more than 33 students.")

    def remove_student(self, Student):
        if Student in self._students:
            self._students.pop(self._students.index(Student))
        else:
            raise Exception


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime, OCT_PIN: int, ):
        super().__init__(first_name, last_name, DOB)
        self._OCT_PIN = OCT_PIN
        self._school = ""
        self._email_k12 = f"{self._first_name.lower()}.{self._last_name.lower()}@ycdsb.ca"
        self._classes = []
    
    def set_OCT_PIN(self, OCT_PIN):
        self._OCT_PIN = OCT_PIN
    
    def get_OCT_PIN(self):
        return self._OCT_PIN
    
    def set_school(self, school):
        self._school = school

    def get_school(self):
        return self._school
    
    def assign_work(self, Class):
        if Class not in self._classes:
            raise Exception
        else:
            class_number = 0
            count = 0
            for c in self._classes:
                if c == Class:
                    class_number = count
                count += 1

            return f"{self._first_name} {self._last_name} assigns work to {self._classes[class_number]._name} class."

    def greet(self):
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a teacher."

    def get_classes(self):
        return self._classes

    def add_class(self, Class):
        if len(self._classes) == 6:
            raise Exception
        else:
            if Class in self._classes:
                raise Exception
            else:
                self._classes.append(Class)


    def remove_class(self, Class):
        self._classes.pop(self._classes.index(Class))

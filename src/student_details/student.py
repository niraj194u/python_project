# student.py

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

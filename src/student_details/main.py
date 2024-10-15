# main.py

from student_details.student import Student

def main():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    grade = input("Enter grade: ")

    student = Student(name, roll_number, grade)
    print(student.get_details())

if __name__ == "__main__":
    main()

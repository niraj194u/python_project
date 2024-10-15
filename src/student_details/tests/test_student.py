# tests/test_student.py

import unittest
from student_details.student import Student

class TestStudent(unittest.TestCase):
    def test_get_details(self):
        student = Student("John Doe", "123", "A")
        self.assertEqual(student.get_details(), "Name: John Doe, Roll Number: 123, Grade: A")

if __name__ == '__main__':
    unittest.main()

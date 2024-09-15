# tests/test_student.py

from student import Student

def test_student_inheritance():
    student = Student("Jane", "Doe")
    assert student.first_name == "Jane"
    assert student.last_name == "Doe"
    assert student.knowledge == []

def test_student_learn():
    student = Student("Jane", "Doe")
    student.learn("Python is fun!")
    assert "Python is fun!" in student.knowledge

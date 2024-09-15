# tests/test_teacher.py

from teacher import Teacher

def test_teacher_inheritance():
    teacher = Teacher("John", "Smith")
    assert teacher.first_name == "John"
    assert teacher.last_name == "Smith"
    assert isinstance(teacher.knowledge, list)

def test_teacher_teach():
    teacher = Teacher("John", "Smith")
    lesson = teacher.teach()
    assert lesson in teacher.knowledge

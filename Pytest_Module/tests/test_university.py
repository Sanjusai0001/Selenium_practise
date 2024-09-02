import pytest
from ..source.university import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def harry_potter_classroom():
    teacher = Teacher("Minerva McGonagall")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
        Student("Draco Malfoy")
    ]
    course_title = "Transfiguration"
    return Classroom(teacher, students, course_title)

def test_add_student(harry_potter_classroom):
    harry_potter_classroom.add_student(Student("Neville Longbottom"))
    assert any(student.name == "Neville Longbottom" for student in harry_potter_classroom.students)

def test_add_student_raises_exception(harry_potter_classroom):
    # Add enough students to exceed the limit
    for i in range(96):
        harry_potter_classroom.add_student(Student(f"Student {i}"))

    with pytest.raises(TooManyStudents):
        harry_potter_classroom.add_student(Student("Overflow Student"))

def test_remove_student(harry_potter_classroom):
    harry_potter_classroom.remove_student("Draco Malfoy")
    assert not any(student.name == "Draco Malfoy" for student in harry_potter_classroom.students)

def test_remove_student_not_exists(harry_potter_classroom):
    harry_potter_classroom.remove_student("Albus Dumbledore")
    assert len(harry_potter_classroom.students) == 4  # No student should be removed

def test_change_teacher(harry_potter_classroom):
    harry_potter_classroom.change_teacher(Teacher("Severus Snape"))
    assert harry_potter_classroom.teacher.name == "Severus Snape"

@pytest.mark.parametrize("new_teacher_name", ["Severus Snape", "Albus Dumbledore", "Gilderoy Lockhart"])
def test_change_teacher_parametrize(harry_potter_classroom, new_teacher_name):
    harry_potter_classroom.change_teacher(Teacher(new_teacher_name))
    assert harry_potter_classroom.teacher.name == new_teacher_name

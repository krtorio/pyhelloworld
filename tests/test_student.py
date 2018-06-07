import pytest
from student import Student

def test_get_student():
	student = Student('Karlo',37)
	assert student.get_age_formatted == "37 years old"


def test_set_student_age():
	student = Student('Karlo',37)
	student.age = 38
	assert student.get_age_formatted == "38 years old"
from student_utils import (
    calculate_average,
    find_top_student,
    get_grade,
    is_passed,
)


def test_calculate_average_basic() -> None:
    assert calculate_average([80.0, 90.0, 100.0]) == 90.0


def test_calculate_average_empty() -> None:
    assert calculate_average([]) == 0.0


def test_get_grade_a() -> None:
    assert get_grade(95.0) == "A"


def test_get_grade_boundary() -> None:
    assert get_grade(89.0) == "B"


def test_is_passed_true() -> None:
    assert is_passed(40.0) is True


def test_is_passed_false() -> None:
    assert is_passed(39.0) is False


def test_find_top_student_basic() -> None:
    students = {
        "Neel": 85.0,
        "Rahul": 92.0,
        "Amit": 78.0,
    }

    assert find_top_student(students) == "Rahul"


def test_find_top_student_empty() -> None:
    assert find_top_student({}) is None

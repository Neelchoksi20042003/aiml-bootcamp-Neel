"""Provide utility functions for working with student data."""


def calculate_average(marks: list[float]) -> float:
    """Calculate the average of a student's marks.

    Args:
        marks: A list of marks. May be empty.

    Returns:
        The average mark as a float, or 0.0 if the list is empty.
    """
    if not marks:
        return 0.0

    return sum(marks) / len(marks)


def get_grade(average: float) -> str:
    """Return the letter grade for an average mark.

    Args:
        average: The student's average mark.

    Returns:
        The corresponding letter grade.
    """
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"

    return "F"


def is_passed(average: float) -> bool:
    """Return whether a student has passed.

    Args:
        average: The student's average mark.

    Returns:
        True if the average is at least 40, otherwise False.
    """
    return average >= 40


def find_top_student(students: dict[str, float]) -> str | None:
    """Return the name of the student with the highest average.

    Args:
        students: A dictionary mapping student names to average marks.

    Returns:
        The name of the student with the highest average,
        or None if the dictionary is empty.
    """
    if not students:
        return None

    return max(students, key=lambda name: students[name])

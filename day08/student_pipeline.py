```python
import csv
import re
from collections import Counter, defaultdict
from datetime import datetime


def load_records(path: str) -> list[dict[str, str]]:
    """Load student records from a CSV file.

    Args:
        path: Path to the CSV file.

    Returns:
        A list of dictionaries containing student records.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    with open(path, "r", newline="") as file:
        return list(csv.DictReader(file))


def extract_email_domain(email: str) -> str | None:
    """Extract the domain from an email address.

    Args:
        email: Email address to examine.

    Returns:
        The extracted domain, or None if no domain is found.
    """
    pattern = r"@([\w.]+)"
    match = re.search(pattern, email)

    if match:
        return match.group(1)

    return None


def normalize_name(name: str) -> str:
    """Normalize a student's name.

    Args:
        name: Student name that may contain extra whitespace
            or inconsistent capitalization.

    Returns:
        A stripped and title-cased student name.
    """
    return name.strip().title()


def parse_enrollment_date(date_text: str) -> datetime:
    """Convert an enrollment date string into a datetime object.

    Args:
        date_text: Date in YYYY-MM-DD format.

    Returns:
        The parsed datetime object.

    Raises:
        ValueError: If the date does not match YYYY-MM-DD format.
    """
    return datetime.strptime(date_text, "%Y-%m-%d")


def find_missing_marks(
    rows: list[dict[str, str]],
) -> list[str]:
    """Find students with at least one missing exam mark.

    Args:
        rows: Student record dictionaries.

    Returns:
        Roll numbers of students with missing marks.
    """
    missing_rolls = []

    for row in rows:
        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam].strip() == "":
                missing_rolls.append(row["roll"])
                break

    return missing_rolls


def count_domains(
    rows: list[dict[str, str]],
) -> Counter[str]:
    """Count student records by email domain.

    Args:
        rows: Student record dictionaries.

    Returns:
        Counter containing the number of records per domain.
    """
    counts = Counter()

    for row in rows:
        domain = extract_email_domain(row["email"])

        if domain is not None:
            counts[domain] += 1

    return counts


def group_by_domain(
    rows: list[dict[str, str]],
) -> defaultdict[str, list[dict[str, str]]]:
    """Group student records by email domain.

    Args:
        rows: Student record dictionaries.

    Returns:
        A defaultdict mapping each email domain to its students.
    """
    grouped = defaultdict(list)

    for row in rows:
        domain = extract_email_domain(row["email"])

        if domain is not None:
            grouped[domain].append(row)

    return grouped


def count_enrollments_by_month(
    rows: list[dict[str, str]],
) -> Counter[str]:
    """Count student enrollments for each calendar month.

    Args:
        rows: Student record dictionaries.

    Returns:
        Counter containing enrollment counts by YYYY-MM.
    """
    counts = Counter()

    for row in rows:
        enrolled = parse_enrollment_date(row["enrolled"])
        month = enrolled.strftime("%Y-%m")
        counts[month] += 1

    return counts
```

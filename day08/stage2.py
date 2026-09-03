import csv
import re
from collections import Counter, defaultdict
from datetime import datetime


def load_records(path):
    """Load student records from a CSV file."""
    with open(path, "r", newline="") as f:
        return list(csv.DictReader(f))


def extract_email_domain(email):
    """Extract the email domain using a regex capture group."""
    pattern = r"@([\w.]+)"
    match = re.search(pattern, email)

    if match:
        return match.group(1)

    return None


def main():
    """Load, clean, parse, and summarize student records."""

    rows = load_records("records.csv")

    print("Total records loaded:", len(rows))

    # Count students by email domain.
    domain_counts = Counter()

    # Group complete student records by email domain.
    students_by_domain = defaultdict(list)

    # Count enrollments by month.
    enrollment_by_month = Counter()

    # Store malformed email rolls.
    malformed_email_rolls = []

    # Store rows containing missing marks.
    missing_mark_rows = []

    for row in rows:

        # Normalize every name by removing surrounding whitespace
        # and using title case.
        row["name"] = row["name"].strip().title()

        # Extract email domain using regex.
        domain = extract_email_domain(row["email"])

        if domain is None:
            malformed_email_rolls.append(row["roll"])
        else:
            domain_counts[domain] += 1
            students_by_domain[domain].append(row)

        # Parse enrollment date into a datetime object.
        enrolled_date = datetime.strptime(
            row["enrolled"],
            "%Y-%m-%d"
        )

        row["enrolled"] = enrolled_date

        # Count students enrolled in each month.
        month = enrolled_date.strftime("%Y-%m")
        enrollment_by_month[month] += 1

        # Handle missing marks deliberately.
        # We keep the row instead of dropping it because a missing
        # mark should not cause us to lose the student's other data.
        # Stage 3 will calculate averages using available marks.
        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam].strip() == "":
                missing_mark_rows.append(row["roll"])
                break

    print("\n===== EMAIL DOMAIN COUNTS =====")

    for domain, count in domain_counts.items():
        print(domain, ":", count)

    print("\n===== MALFORMED EMAILS =====")

    print("Number of malformed emails:", len(malformed_email_rolls))
    print("Rolls:", malformed_email_rolls)

    print("\n===== ENROLLMENTS BY MONTH =====")

    for month, count in sorted(enrollment_by_month.items()):
        print(month, ":", count)

    print("\n===== STUDENTS BY EMAIL DOMAIN =====")

    for domain, students in students_by_domain.items():
        print(domain, ":", len(students), "students")

    print("\n===== MISSING MARKS =====")

    print("Students with missing marks:", len(missing_mark_rows))
    print("Rolls:", missing_mark_rows)

    print("\n===== SAMPLE NORMALIZED RECORD =====")
    print(rows[0])

    print("\nTASK 03 STAGE 2 COMPLETED")


if __name__ == "__main__":
    main()
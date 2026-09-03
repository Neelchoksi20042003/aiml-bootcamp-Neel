import csv

input_file = "records.csv"

required_columns = [
    "roll",
    "name",
    "email",
    "enrolled",
    "exam1",
    "exam2",
    "exam3",
    "exam4"
]

errors = []

with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)

    # Check columns
    if reader.fieldnames != required_columns:
        errors.append("Incorrect CSV columns")

    rows = list(reader)

# Check number of students
if len(rows) != 200:
    errors.append(
        f"Expected 200 students, found {len(rows)}"
    )

# Check duplicate rolls
rolls = [row["roll"] for row in rows]

if len(rolls) != len(set(rolls)):
    errors.append("Duplicate roll numbers found")

# Check missing marks
missing_marks = 0

for row in rows:
    for exam in ["exam1", "exam2", "exam3", "exam4"]:
        if row[exam] == "":
            missing_marks += 1

# Check malformed emails
bad_emails = 0

for row in rows:
    email = row["email"]

    if "@" not in email or "." not in email.split("@")[-1]:
        bad_emails += 1


print("\n===== VALIDATION REPORT =====")

print("Total rows:", len(rows))
print("Missing marks:", missing_marks)
print("Malformed emails:", bad_emails)

if errors:
    print("\nERRORS FOUND:")

    for error in errors:
        print("-", error)

else:
    print("\nBasic structure validation: PASSED")

print("\nData-quality validation completed.")
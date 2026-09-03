import csv

input_file = "records.csv"
output_file = "cleaned_records.csv"

cleaned_rows = []
missing_marks = []
bad_emails = []

with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Clean the student's name
        row["name"] = row["name"].strip().title()

        # Check for missing exam marks
        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam].strip() == "":
                missing_marks.append(
                    (row["roll"], row["name"], exam)
                )

        # Check email format
        email = row["email"].strip()

        if "@" not in email or "." not in email.split("@")[-1]:
            bad_emails.append(
                (row["roll"], row["name"], email)
            )

        # Convert available marks to integers
        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam].strip() != "":
                row[exam] = int(row[exam])

        cleaned_rows.append(row)


# Display problems found
print("\n===== DATA QUALITY REPORT =====")

print("\nMissing marks:")
for item in missing_marks:
    print(item)

print("\nMalformed emails:")
for item in bad_emails:
    print(item)

print("\nTotal missing marks:", len(missing_marks))
print("Total malformed emails:", len(bad_emails))


# Write cleaned data
with open(output_file, "w", newline="") as f:
    fieldnames = [
        "roll",
        "name",
        "email",
        "enrolled",
        "exam1",
        "exam2",
        "exam3",
        "exam4"
    ]

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(cleaned_rows)


print("\nCleaned data saved to:", output_file)

import csv

input_file = "cleaned_records.csv"
output_file = "student_report.csv"

students = []

# Read cleaned data
with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Collect available marks
        marks = []

        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam].strip() != "":
                marks.append(int(row[exam]))

        # Calculate average
        if marks:
            average = sum(marks) / len(marks)
        else:
            average = 0

        # Calculate total
        total = sum(marks)

        # Pass/fail
        if average >= 40:
            status = "PASS"
        else:
            status = "FAIL"

        # Add calculated values
        row["total"] = total
        row["average"] = round(average, 2)
        row["status"] = status

        students.append(row)


# Sort students from highest average to lowest
students.sort(
    key=lambda student: student["average"],
    reverse=True
)


# Assign ranks
for rank, student in enumerate(students, start=1):
    student["rank"] = rank


# Display top 10 students
print("\n===== TOP 10 STUDENTS =====")

for student in students[:10]:
    print(
        f"Rank {student['rank']}: "
        f"{student['name']} - "
        f"Average: {student['average']}"
    )


# Create final report
fieldnames = [
    "rank",
    "roll",
    "name",
    "email",
    "enrolled",
    "exam1",
    "exam2",
    "exam3",
    "exam4",
    "total",
    "average",
    "status"
]


with open(output_file, "w", newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(students)


print("\nFinal report created:", output_file)
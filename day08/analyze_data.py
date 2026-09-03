import csv

input_file = "cleaned_records.csv"

students = []

with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:

        marks = []

        for exam in ["exam1", "exam2", "exam3", "exam4"]:
            if row[exam] != "":
                marks.append(int(row[exam]))

        # Calculate average using available marks
        if marks:
            average = sum(marks) / len(marks)
        else:
            average = 0

        # Calculate total using available marks
        total = sum(marks)

        # Determine pass/fail
        if average >= 40:
            status = "PASS"
        else:
            status = "FAIL"

        # Add calculated information
        row["total"] = total
        row["average"] = round(average, 2)
        row["status"] = status

        students.append(row)


# Find highest scorer
highest = max(students, key=lambda student: student["average"])

# Find lowest scorer
lowest = min(students, key=lambda student: student["average"])

# Calculate class average
class_average = sum(
    student["average"] for student in students
) / len(students)

# Count pass and fail
passed = sum(
    1 for student in students
    if student["status"] == "PASS"
)

failed = sum(
    1 for student in students
    if student["status"] == "FAIL"
)


# Display report
print("\n===== STUDENT PERFORMANCE REPORT =====")

print(f"Total students: {len(students)}")

print(f"Class average: {class_average:.2f}")

print(f"Passed students: {passed}")

print(f"Failed students: {failed}")

print("\n===== HIGHEST SCORER =====")

print("Roll:", highest["roll"])
print("Name:", highest["name"])
print("Average:", highest["average"])

print("\n===== LOWEST SCORER =====")

print("Roll:", lowest["roll"])
print("Name:", lowest["name"])
print("Average:", lowest["average"])
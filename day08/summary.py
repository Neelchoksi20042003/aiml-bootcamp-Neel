import csv

input_file = "student_report.csv"

students = []

with open(input_file, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        students.append(row)


total_students = len(students)

passed = sum(
    1 for student in students
    if student["status"] == "PASS"
)

failed = sum(
    1 for student in students
    if student["status"] == "FAIL"
)

class_average = sum(
    float(student["average"])
    for student in students
) / total_students


print("\n===================================")
print("       STUDENT PERFORMANCE REPORT")
print("===================================")

print(f"Total students : {total_students}")
print(f"Passed         : {passed}")
print(f"Failed         : {failed}")
print(f"Class average  : {class_average:.2f}")

print("\nTop 5 Students")
print("-----------------------------------")

for student in students[:5]:
    print(
        f"{student['rank']}. "
        f"{student['name']} - "
        f"{student['average']}"
    )

print("\n===================================")
import csv
import numpy as np


def load_records(path):
    """Load student records from a CSV file."""
    with open(path, "r", newline="") as f:
        return list(csv.DictReader(f))


rows = load_records("records.csv")

marks = np.array(
    [
        [
            float(row[f"exam{i}"]) if row[f"exam{i}"] != "" else np.nan
            for i in range(1, 5)
        ]
        for row in rows
    ]
)

print("Marks shape:", marks.shape)
print("\nMarks array:")
print(marks)


per_student = np.nanmean(marks, axis=1)

per_exam = np.nanmean(marks, axis=0)

print("\nStudent averages:")
print(per_student)

print("\nExam averages:")
print(per_exam)

np.nanmean(marks, axis=1)
np.nanmean(marks, axis=0)

passed = per_student >= 60

pass_count = np.sum(passed)

pass_proportion = pass_count / len(per_student)

print("\n===== PASSING STUDENTS =====")
print("Students passed:", pass_count)
print("Pass proportion:", pass_proportion)
print("Pass percentage:", pass_proportion * 100)


top10 = per_student.argsort()[::-1][:10]


top10_indices = per_student.argsort()[::-1][:10]

print("\n===== TOP 10 STUDENTS =====")

for rank, index in enumerate(top10_indices, start=1):
    print(
        f"{rank}. {rows[index]['name']} "
        f"- Average: {per_student[index]:.2f}"
    )

exam_names = np.array(["exam1", "exam2", "exam3", "exam4"])

hardest_index = np.argmin(per_exam)
hardest_exam = exam_names[hardest_index]

exam_std = np.nanstd(marks, axis=0)

widest_index = np.argmax(exam_std)
widest_exam = exam_names[widest_index]

print("\n===== EXAM ANALYSIS =====")

print("Exam averages:")
for name, average in zip(exam_names, per_exam):
    print(f"{name}: {average:.2f}")

print(f"\nHardest exam: {hardest_exam}")
print(f"Hardest exam average: {per_exam[hardest_index]:.2f}")

print("\nExam standard deviations:")
for name, std in zip(exam_names, exam_std):
    print(f"{name}: {std:.2f}")

print(f"\nWidest spread: {widest_exam}")
print(f"Widest spread standard deviation: {exam_std[widest_index]:.2f}")

exam_means = np.nanmean(marks, axis=0)
exam_stds = np.nanstd(marks, axis=0)

standardized_marks = (marks - exam_means) / exam_stds

print("\n===== STANDARDIZED MARKS =====")
print(standardized_marks)

curved_marks = np.minimum(marks + 5, 100)

cap_count = np.sum(curved_marks == 100)

print("\n===== CURVED MARKS =====")
print(curved_marks)

print("\nNumber of marks that hit 100:", cap_count)

domains = np.array(
    [
        row["email"].split("@")[-1]
        for row in rows
    ]
)

unique_domains, domain_codes = np.unique(
    domains,
    return_inverse=True
)

domain_totals = np.bincount(
    domain_codes,
    weights=per_student
)

domain_counts = np.bincount(domain_codes)

domain_averages = domain_totals / domain_counts

print("\n===== PERFORMANCE BY EMAIL DOMAIN =====")

for domain, average, count in zip(
    unique_domains,
    domain_averages,
    domain_counts
):
    print(
        f"{domain}: Average = {average:.2f}, "
        f"Students = {count}"
    )

highest_domain_index = np.argmax(domain_averages)
lowest_domain_index = np.argmin(domain_averages)

print(
    f"\nHighest average domain: "
    f"{unique_domains[highest_domain_index]} "
    f"({domain_averages[highest_domain_index]:.2f})"
)

print(
    f"Lowest average domain: "
    f"{unique_domains[lowest_domain_index]} "
    f"({domain_averages[lowest_domain_index]:.2f})"
)

domain_difference = (
    domain_averages[highest_domain_index]
    - domain_averages[lowest_domain_index]
)

print(
    f"Difference between highest and lowest: "
    f"{domain_difference:.2f} marks"
)
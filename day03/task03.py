from itertools import combinations, permutations, product
# TASK 03 - COMBINATIONS WITH ITERTOOLS

# TASK 1: Generate every possible pair of students

students = [
    "asha",
    "ravi",
    "meera",
    "dev",
    "priya"
]

pairs = list(combinations(students, 2))

print("===== COMBINATIONS =====")
for pair in pairs:
    print(pair)

print("Number of pairs:", len(pairs))

# Formula:
# nCr = n! / (r! * (n-r)!)
# 5C2 = 5! / (2! * 3!)
#     = 10
# The calculated count matches itertools.combinations.
# TASK 2: Generate every ordered pair

ordered_pairs = list(
    permutations(students, 2)
)

print("\n===== PERMUTATIONS =====")

for pair in ordered_pairs:
    print(pair)

print("Number of ordered pairs:", len(ordered_pairs))

# Formula:
# nPr = n! / (n-r)!
# 5P2 = 5! / 3!
#     = 20
# Permutations produce more results because order matters.
# (asha, ravi) and (ravi, asha) are different permutations.


# TASK 3: Product of shirt colours and sizes

colours = [
    "red",
    "blue",
    "green"
]

sizes = [
    "S",
    "M"
]

shirts = list(
    product(colours, sizes)
)

print("\n===== SHIRT PRODUCTS =====")

for shirt in shirts:
    print(shirt)

print("Number of combinations:", len(shirts))

# 3 colours × 2 sizes = 6 possible products.
# TASK 4: All possible feature subsets

features = [
    "age",
    "income",
    "education",
    "experience"
]

all_subsets = []

for r in range(len(features) + 1):
    all_subsets.extend(
        combinations(features, r)
    )

print("\n===== ALL FEATURE SUBSETS =====")

for subset in all_subsets:
    print(subset)

print("Number of subsets:", len(all_subsets))

# Each feature has two choices:
# include it OR exclude it.
# Therefore:
# 2^4 = 16
# The result should contain exactly 16 subsets.
# FINAL CHECK
print("\n===== FINAL CHECK =====")
print("Student pairs:", len(pairs))
print("Ordered pairs:", len(ordered_pairs))
print("Shirt products:", len(shirts))
print("Feature subsets:", len(all_subsets))
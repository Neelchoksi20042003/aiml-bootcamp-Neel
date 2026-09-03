import numpy as np


# ==================================================
# 1. Create dataset
# ==================================================

rng = np.random.default_rng(0)

height_cm = rng.normal(170, 10, 100)

# Exactly dependent on height_cm
height_in = height_cm / 2.54

weight = rng.normal(70, 15, 100)

age = rng.integers(20, 60, 100)

income = rng.normal(50000, 10000, 100)


# ==================================================
# 2. Build feature matrix
# ==================================================

X = np.column_stack([
    height_cm,
    height_in,
    weight,
    age,
    income
])


print("=" * 60)
print("FEATURE MATRIX")
print("=" * 60)

print("Shape:", X.shape)


# ==================================================
# 3. Calculate rank
# ==================================================

rank = np.linalg.matrix_rank(X)

print("\n" + "=" * 60)
print("MATRIX RANK")
print("=" * 60)

print("Number of features:", X.shape[1])
print("Matrix rank:", rank)


# ==================================================
# 4. Check correlations
# ==================================================

feature_names = [
    "height_cm",
    "height_in",
    "weight",
    "age",
    "income"
]

correlation_matrix = np.corrcoef(X, rowvar=False)

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

print(correlation_matrix)


# ==================================================
# 5. Identify highly correlated features
# ==================================================

print("\n" + "=" * 60)
print("HIGH CORRELATIONS")
print("=" * 60)

for i in range(len(feature_names)):
    for j in range(i + 1, len(feature_names)):

        correlation = correlation_matrix[i, j]

        if abs(correlation) > 0.99:
            print(
                f"{feature_names[i]} <-> {feature_names[j]} "
                f"= {correlation:.6f}"
            )


# ==================================================
# 6. Drop height_in
# ==================================================

X_reduced = np.column_stack([
    height_cm,
    weight,
    age,
    income
])


reduced_rank = np.linalg.matrix_rank(X_reduced)

print("\n" + "=" * 60)
print("AFTER REMOVING REDUNDANT FEATURE")
print("=" * 60)

print("New number of features:", X_reduced.shape[1])
print("New matrix rank:", reduced_rank)


# ==================================================
# 7. Verify the relationship
# ==================================================

calculated_height_in = height_cm / 2.54

difference = np.max(
    np.abs(height_in - calculated_height_in)
)

print("\n" + "=" * 60)
print("DEPENDENCY CHECK")
print("=" * 60)

print("Maximum difference:", difference)

if difference == 0:
    print("height_in is exactly dependent on height_cm.")


# ==================================================
# 8. Final conclusion
# ==================================================

print("\n" + "=" * 60)
print("CONCLUSION")
print("=" * 60)

print(
    "height_in is redundant because it can be calculated "
    "exactly from height_cm."
)

print(
    "Removing height_in restores full rank to the feature matrix."
)
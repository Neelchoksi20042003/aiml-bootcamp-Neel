import numpy as np
import matplotlib.pyplot as plt

# Each column represents one (x, y) point.
shape = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
], dtype=float)

def show_transform(matrix, title):
    # Matrix multiplication applies the transformation to every point.
    transformed = matrix @ shape

    fig, axes = plt.subplots(1, 2, figsize=(9, 4))

    # Original shape
    axes[0].plot(shape[0], shape[1], marker="o")
    axes[0].set_title("Before")

    # Transformed shape
    axes[1].plot(transformed[0], transformed[1], marker="o")
    axes[1].set_title("After")

    for ax in axes:
        ax.axhline(0)
        ax.axvline(0)
        ax.grid(True)
        ax.set_aspect("equal")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

# MATRICES FROM TASK 01
# Scaling: x stretches by 2 and y shrinks by 0.5.
scaling = np.array([
    [2, 0],
    [0, 0.5]
])

# Rotation matrix.
def rotation(degrees):
    theta = np.radians(degrees)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# Use the 30° rotation from Task 01.
rotation_matrix = rotation(30)

# Shear: y stays unchanged while x shifts.
shear = np.array([
    [1, 1],
    [0, 1]
])

# Reflection across the x-axis.
reflection = np.array([
    [1, 0],
    [0, -1]
])

# TASK 2 — COMPUTE DETERMINANTS

print("=" * 60)
print("TASK 2 — DETERMINANTS AND INVERTIBILITY")
print("=" * 60)


# Compute and display the determinant of each matrix.
matrices = {
    "Scaling": scaling,
    "Rotation": rotation_matrix,
    "Shear": shear,
    "Reflection": reflection
}


for name, matrix in matrices.items():
    det = np.linalg.det(matrix)

    print(f"{name}:")
    print(matrix)
    print(f"Determinant: {det:.2f}")
    print()

# CHECK THE EXPECTED DETERMINANTS

print("=" * 60)
print("EXPECTED RESULTS")
print("=" * 60)

print(f"Scaling determinant: {np.linalg.det(scaling):.2f}")
print(f"Rotation determinant: {np.linalg.det(rotation_matrix):.2f}")
print(f"Shear determinant: {np.linalg.det(shear):.2f}")
print(f"Reflection determinant: {np.linalg.det(reflection):.2f}")

# SINGULAR MATRIX
print("\n" + "=" * 60)
print("SINGULAR MATRIX")
print("=" * 60)

# The second column is 2 times the first column.
# Therefore, the columns are linearly dependent.
singular = np.array([
    [1., 2.],
    [2., 4.]
])

singular_det = np.linalg.det(singular)
print("Singular matrix:")
print(singular)

print(f"Determinant: {singular_det:.2f}")

# Apply the singular matrix to the square.
show_transform(
    singular,
    "Singular Matrix Transformation"
)

# TRY TO INVERT THE SINGULAR MATRIX

print("Trying to invert the singular matrix...")

try:
    inverse_singular = np.linalg.inv(singular)
    print(inverse_singular)

except np.linalg.LinAlgError as error:
    print("Error:", error)

# CHECK WHETHER A MATRIX IS INVERTIBLE

def is_invertible(matrix):
    # A determinant of zero means the transformation cannot be undone.
    return not np.isclose(np.linalg.det(matrix), 0)

# TEST ALL FIVE MATRICES

print("\n" + "=" * 60)
print("INVERTIBILITY CHECK")
print("=" * 60)


all_matrices = {
    "Scaling": scaling,
    "Rotation": rotation_matrix,
    "Shear": shear,
    "Reflection": reflection,
    "Singular": singular
}


for name, matrix in all_matrices.items():
    print(
        f"{name}: "
        f"Determinant = {np.linalg.det(matrix):.2f}, "
        f"Invertible = {is_invertible(matrix)}"
    )

# FINAL OBSERVATIONS

print("\n" + "=" * 60)
print("FINAL OBSERVATIONS")
print("=" * 60)

print("Scaling    -> determinant = 1   -> area unchanged")
print("Rotation   -> determinant = 1   -> area unchanged")
print("Shear      -> determinant = 1   -> area unchanged")
print("Reflection -> determinant = -1  -> orientation reversed")
print("Singular   -> determinant = 0   -> transformation not invertible")
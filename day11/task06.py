import numpy as np
import matplotlib.pyplot as plt

# TASK 06: INTERACTIVE TRANSFORMATION EXPLORER

# STEP 1: Create our square shape

shape = np.array([
    [0, 0],
    [2, 0],
    [2, 2],
    [0, 2],
    [0, 0]
])

# STEP 2: Transformation explorer function

def explore(a, b, c, d):

    # Create the 2x2 matrix
    M = np.array([
        [a, b],
        [c, d]
    ], dtype=float)

    # Apply matrix to shape

    transformed = (M @ shape.T).T

    # Basis vectors

    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.0, 1.0])

    e1_transformed = M @ e1
    e2_transformed = M @ e2

    # Determinant

    determinant = np.linalg.det(M)

    # Print information
    
    print("======================================")
    print("TRANSFORMATION EXPLORER")
    print("======================================")
    print("\nMatrix M:")
    print(M)
    print("\nFirst column = where e1 lands:")
    print(e1_transformed)
    print("\nSecond column = where e2 lands:")
    print(e2_transformed)
    print("\nDeterminant:")
    print(determinant)

    # Plot

    plt.figure(figsize=(8, 8))

    # Original shape
    plt.plot(
        shape[:, 0],
        shape[:, 1],
        'k--',
        marker='o',
        label='Original'
    )

    # Transformed shape
    plt.plot(
        transformed[:, 0],
        transformed[:, 1],
        marker='o',
        label='Transformed'
    )

    # Original basis vectors
    plt.quiver(
        0, 0,
        1, 0,
        angles='xy',
        scale_units='xy',
        scale=1,
        label='Original e1'
    )

    plt.quiver(
        0, 0,
        0, 1,
        angles='xy',
        scale_units='xy',
        scale=1,
        label='Original e2'
    )

    # Transformed basis vectors
    plt.quiver(
        0, 0,
        e1_transformed[0],
        e1_transformed[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        label='M @ e1'
    )

    plt.quiver(
        0, 0,
        e2_transformed[0],
        e2_transformed[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        label='M @ e2'
    )

    # Axes
    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(
        f"Matrix Transformation\n"
        f"det(M) = {determinant:.2f}"
    )
    plt.legend()
    plt.show()

# EXPERIMENT 1: PURE ROTATION

print("\n\nEXPERIMENT 1: PURE ROTATION")

angle = np.radians(45)

explore(
    np.cos(angle),
    -np.sin(angle),
    np.sin(angle),
    np.cos(angle)
)

# EXPERIMENT 2: PURE SCALING

print("\n\nEXPERIMENT 2: PURE SCALING")

explore(
    2,
    0,
    0,
    2
)

# EXPERIMENT 3: REFLECTION

print("\n\nEXPERIMENT 3: REFLECTION")

explore(
    -1,
    0,
    0,
    1
)

# EXPERIMENT 4: NEGATIVE DETERMINANT

print("\n\nEXPERIMENT 4: NEGATIVE DETERMINANT")

explore(
    -2,
    0,
    0,
    2
)

# EXPERIMENT 5: SINGULAR MATRIX

print("\n\nEXPERIMENT 5: COLLAPSE TO A LINE")

explore(
    1,
    2,
    2,
    4
)

# REFERENCE TABLE

print("\n\n======================================")
print("REFERENCE TABLE")
print("======================================")

matrices = [
    ("45° Rotation", [0.7071, -0.7071, 0.7071, 0.7071]),
    ("Scaling ×2", [2, 0, 0, 2]),
    ("Reflection X", [-1, 0, 0, 1]),
    ("Negative Scaling", [-2, 0, 0, 2]),
    ("Collapse to Line", [1, 2, 2, 4])
]

print(
    f"{'Matrix':<20}"
    f"{'a':>8}"
    f"{'b':>8}"
    f"{'c':>8}"
    f"{'d':>8}"
    f"{'det':>12}"
)

print("-" * 70)
for name, values in matrices:

    a, b, c, d = values
    M = np.array([
        [a, b],
        [c, d]
    ])

    determinant = np.linalg.det(M)
    print(
        f"{name:<20}"
        f"{a:>8.4f}"
        f"{b:>8.4f}"
        f"{c:>8.4f}"
        f"{d:>8.4f}"
        f"{determinant:>12.4f}"
    )
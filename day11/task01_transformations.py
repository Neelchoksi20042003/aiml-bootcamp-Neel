import numpy as np
import matplotlib.pyplot as plt


# Each column represents one (x, y) point of the shape.
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

    # Keep the same scale on both axes so the geometry is not distorted.
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

    print("Transformation matrix:")
    print(matrix)

    # Determinant tells us how the transformation changes area.
    print("Determinant:", np.linalg.det(matrix))
    print("-" * 50)

# TASK 01 — VISUALISE THE FOUR TRANSFORMATIONS
# 1. SCALING
# x is multiplied by 2 and y is multiplied by 0.5.
# The square becomes wider and shorter.

scaling = np.array([
    [2, 0],
    [0, 0.5]
])

show_transform(scaling, "Scaling")

# 2. ROTATION
# Convert degrees to radians because NumPy's sin/cos use radians.
# This matrix rotates points counterclockwise.

def rotation(degrees):
    theta = np.radians(degrees)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# Rotate by 30 degrees
R30 = rotation(30)
show_transform(R30, "Rotation 30°")

# Rotate by 90 degrees
R90 = rotation(90)
show_transform(R90, "Rotation 90°")

# Rotate by 180 degrees
R180 = rotation(180)
show_transform(R180, "Rotation 180°")

# 3. SHEAR
# x' = x + y
# y' = y
# Therefore, y stays unchanged while x shifts horizontally.

shear = np.array([
    [1, 1],
    [0, 1]
])

show_transform(shear, "Shear")

# 4. REFLECTION

# Reflection across the X-axis:
# x stays the same and y changes sign.

reflection_x = np.array([
    [1, 0],
    [0, -1]
])

show_transform(
    reflection_x,
    "Reflection across X-axis"
)

# Reflection across the Y-axis:
# y stays the same and x changes sign.

reflection_y = np.array([
    [-1, 0],
    [0, 1]
])

show_transform(
    reflection_y,
    "Reflection across Y-axis"
)

# SUMMARY

print("\nTASK 01 COMPLETE")
print()
print("Scaling:")
print("  x → stretched by 2")
print("  y → shrunk by 0.5")
print("  determinant = 1")
print()
print("Rotation:")
print("  changes orientation")
print("  preserves size and area")
print("  determinant = 1")
print()
print("Shear:")
print("  changes the shape into a parallelogram")
print("  determinant = 1")
print()
print("Reflection:")
print("  flips the shape across an axis")
print("  determinant = -1")
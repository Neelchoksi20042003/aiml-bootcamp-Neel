import numpy as np
import matplotlib.pyplot as plt

# TASK 05: Special Matrices and Their Properties

# Helper function: Rotation matrix

def rotation(degrees):
    theta = np.radians(degrees)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

# PART 1: DIAGONAL MATRIX

# A diagonal matrix
D = np.array([
    [2.0, 0.0],
    [0.0, 3.0]
])

print("========================================")
print("1. DIAGONAL MATRIX")
print("========================================")
print("D =")
print(D)

# Check that the matrix is diagonal
is_diagonal = np.allclose(D, np.diag(np.diag(D)))

print("\nIs D diagonal?")
print(is_diagonal)

# Apply diagonal matrix to a vector
v = np.array([1.0, 1.0])

scaled_v = D @ v

print("\nOriginal vector:")
print(v)

print("\nAfter applying D:")
print(scaled_v)

# PART 2: SYMMETRIC MATRIX

sym = np.array([
    [2.0, 1.0],
    [1.0, 3.0]
])

print("\n========================================")
print("2. SYMMETRIC MATRIX")
print("========================================")
print("Symmetric matrix:")
print(sym)
print("\nTranspose:")
print(sym.T)
print("\nIs symmetric?")
print(np.allclose(sym, sym.T))

# PART 3: ORTHOGONAL MATRIX

Q = rotation(30)
print("\n========================================")
print("3. ORTHOGONAL MATRIX")
print("========================================")
print("Q =")
print(Q)
print("\nQ.T =")
print(Q.T)

# Q.T @ Q should equal identity
identity_check = Q.T @ Q

print("\nQ.T @ Q =")
print(identity_check)
print("\nIdentity matrix:")
print(np.eye(2))
print("\nIs Q orthogonal?")
print(np.allclose(Q.T @ Q, np.eye(2)))

# PART 4: ORTHOGONAL MATRIX PRESERVES LENGTH

v = np.array([3.0, 4.0])

original_length = np.linalg.norm(v)

rotated_v = Q @ v

new_length = np.linalg.norm(rotated_v)

print("\n========================================")
print("4. LENGTH PRESERVATION")
print("========================================")
print("Original vector:")
print(v)
print("\nOriginal length:")
print(original_length)
print("\nRotated vector:")
print(rotated_v)
print("\nLength after rotation:")
print(new_length)
print("\nDoes Q preserve length?")
print(np.isclose(new_length, original_length))

# PART 5: ORTHOGONAL MATRIX PRESERVES ANGLES

v1 = np.array([1.0, 0.0])
v2 = np.array([1.0, 1.0])

# Function to calculate angle between two vectors
def angle_between(a, b):

    cosine = np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

    # Prevent tiny floating-point errors
    cosine = np.clip(cosine, -1.0, 1.0)

    return np.degrees(np.arccos(cosine))

original_angle = angle_between(v1, v2)
# Rotate both vectors
v1_rotated = Q @ v1
v2_rotated = Q @ v2

new_angle = angle_between(v1_rotated, v2_rotated)
print("\n========================================")
print("5. ANGLE PRESERVATION")
print("========================================")
print("Original vectors:")
print("v1 =", v1)
print("v2 =", v2)
print("\nOriginal angle:")
print(original_angle, "degrees")
print("\nRotated vectors:")
print("Q @ v1 =", v1_rotated)
print("Q @ v2 =", v2_rotated)
print("\nAngle after rotation:")
print(new_angle, "degrees")
print("\nDoes Q preserve the angle?")
print(np.isclose(original_angle, new_angle))

# PART 6: PLOT THE EFFECT OF THE ORTHOGONAL MATRIX

plt.figure(figsize=(8, 8))
# Original vectors
plt.quiver(
    0, 0,
    v1[0], v1[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='v1 original'
)

plt.quiver(
    0, 0,
    v2[0], v2[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='v2 original'
)

# Rotated vectors
plt.quiver(
    0, 0,
    v1_rotated[0], v1_rotated[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='Q @ v1'
)

plt.quiver(
    0, 0,
    v2_rotated[0], v2_rotated[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='Q @ v2'
)

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True)
plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Orthogonal Transformation Preserves Length and Angle")
plt.legend()
plt.show()

# PART 7: WHY THIS IS USEFUL IN ML

print("\n========================================")
print("6. ML USE")
print("========================================")
print(
    "Orthogonal matrices are useful in ML because they "
    "preserve vector lengths and angles, helping transformations "
    "avoid unwanted distortion of the data geometry."
)
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Create three 2x2 transformation matrices
# A = Rotation matrix (90 degrees)

theta = np.pi / 2

A = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])


# B = Scaling matrix
B = np.array([
    [2, 0],
    [0, 1.5]
])


# C = Shear matrix
C = np.array([
    [1, 1],
    [0, 1]
])


print("A (Rotation):")
print(A)

print("\nB (Scaling):")
print(B)

print("\nC (Shear):")
print(C)

# STEP 2: Verify associativity


# First grouping: (A @ B) @ C
left = (A @ B) @ C

# Second grouping: A @ (B @ C)
right = A @ (B @ C)


print("\n================ ASSOCIATIVITY ================")

print("\n(A @ B) @ C:")
print(left)

print("\nA @ (B @ C):")
print(right)

print("\nAre they equal?")
print(np.allclose(left, right))

# STEP 3: Verify that matrix multiplication is NOT
# generally commutative

AB = A @ B
BA = B @ A


print("\n================ COMMUTATIVITY ================")

print("\nA @ B:")
print(AB)

print("\nB @ A:")
print(BA)

print("\nAre A @ B and B @ A equal?")
print(np.allclose(AB, BA))

# STEP 4: Create a shape

shape = np.array([
    [0, 0],
    [2, 0],
    [2, 1],
    [0, 1],
    [0, 0]
])

# STEP 5: Apply A @ B 

shape_AB = (A @ B) @ shape.T
shape_AB = shape_AB.T

# STEP 6: Apply B @ A

shape_BA = (B @ A) @ shape.T
shape_BA = shape_BA.T

# STEP 7: Plot original, A @ B, and B @ A

plt.figure(figsize=(8, 8))

# Original shape
plt.plot(
    shape[:, 0],
    shape[:, 1],
    'k--',
    label='Original'
)

# A @ B
plt.plot(
    shape_AB[:, 0],
    shape_AB[:, 1],
    marker='o',
    label='A @ B'
)

# B @ A
plt.plot(
    shape_BA[:, 0],
    shape_BA[:, 1],
    marker='o',
    label='B @ A'
)


plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.grid(True)
plt.axis('equal')

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Non-Commutativity of Matrix Transformations")

plt.legend()

plt.show()
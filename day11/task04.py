import numpy as np
import matplotlib.pyplot as plt

# TASK 04: Compose a Sequence of Transformations

# STEP 1: Create the original shape

shape = np.array([
    [0, 0],
    [2, 0],
    [2, 1],
    [0, 1],
    [0, 0]
])

# STEP 2: Create Scaling Matrix
# Scale by 1.5

S = np.array([
    [1.5, 0],
    [0, 1.5]
])

# STEP 3: Create Rotation Matrix
# Rotate by 45 degrees

theta = np.radians(45)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# STEP 4: Create Shear Matrix

Sh = np.array([
    [1, 0.5],
    [0, 1]
])

# STEP 5: Apply transformations separately

# First: Scale
shape_scaled = (S @ shape.T).T

# Second: Rotate
shape_rotated = (R @ shape_scaled.T).T

# Third: Shear
shape_sheared = (Sh @ shape_rotated.T).T

# STEP 6: Combine all transformations into one matrix

combined = Sh @ R @ S

print("Scaling matrix S:")
print(S)

print("\nRotation matrix R:")
print(R)

print("\nShear matrix Sh:")
print(Sh)

print("\nCombined matrix:")
print(combined)

# STEP 7: Apply combined matrix directly

shape_combined = (combined @ shape.T).T

# STEP 8: Confirm both methods give the same result

print("\n====================================")
print("CHECKING SEPARATE VS COMBINED")
print("====================================")

print("\nShape after separate transformations:")
print(shape_sheared)

print("\nShape after combined transformation:")
print(shape_combined)

print("\nAre they equal?")
print(np.allclose(shape_sheared, shape_combined))

# STEP 9: Calculate determinants

det_S = np.linalg.det(S)
det_R = np.linalg.det(R)
det_Sh = np.linalg.det(Sh)

det_combined = np.linalg.det(combined)

product_of_determinants = det_S * det_R * det_Sh

print("\n====================================")
print("DETERMINANTS")
print("====================================")

print("det(S)  =", det_S)
print("det(R)  =", det_R)
print("det(Sh) =", det_Sh)

print("\nDeterminant of combined matrix:")
print(det_combined)

print("\nProduct of individual determinants:")
print(product_of_determinants)

print("\nDo determinants match?")
print(np.allclose(det_combined, product_of_determinants))

# STEP 10: Plot each stage

plt.figure(figsize=(9, 9))

# Original
plt.plot(
    shape[:, 0],
    shape[:, 1],
    'k--',
    marker='o',
    label='Original'
)

# After scaling
plt.plot(
    shape_scaled[:, 0],
    shape_scaled[:, 1],
    marker='o',
    label='1. Scale × 1.5'
)

# After rotation
plt.plot(
    shape_rotated[:, 0],
    shape_rotated[:, 1],
    marker='o',
    label='2. Rotate 45°'
)

# After shear
plt.plot(
    shape_sheared[:, 0],
    shape_sheared[:, 1],
    marker='o',
    label='3. Shear'
)

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True)
plt.axis('equal')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Composition of Transformations")
plt.legend()
plt.show()
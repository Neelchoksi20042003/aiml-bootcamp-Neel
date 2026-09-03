import numpy as np


def angle_between(a, b):
    """
    Return the angle between two vectors in degrees.
    """

    a = np.asarray(a)
    b = np.asarray(b)

    # Calculate cosine similarity
    cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # Protect against floating-point errors that may push
    # cosine slightly outside the valid range [-1, 1].
    cos = np.clip(cos, -1, 1)

    # Convert cosine value to angle in degrees
    return np.degrees(np.arccos(cos))


# 1. Perpendicular vectors → 90°
v1 = np.array([1, 0])
v2 = np.array([0, 1])

print("Perpendicular:", angle_between(v1, v2))


# 2. Identical vectors → 0°
v1 = np.array([1, 2, 3])
v2 = np.array([1, 2, 3])

print("Identical:", angle_between(v1, v2))


# 3. Opposite vectors → 180°
v1 = np.array([1, 2])
v2 = np.array([-1, -2])

print("Opposite:", angle_between(v1, v2))


# 4. Angle between two students' exam-score vectors
student_A = np.array([80, 75, 90, 85, 95])
student_B = np.array([78, 73, 88, 84, 92])

student_angle = angle_between(student_A, student_B)

print("Student angle:", student_angle, "degrees")

# A small angle means the students have similar performance
# patterns across the subjects.


# 5. Scaling test
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

angle_original = angle_between(a, b)
angle_scaled = angle_between(a, 5 * b)

print("Original angle:", angle_original)
print("Scaled angle:", angle_scaled)

# Scaling b changes its magnitude but not its direction,
# therefore the angle between a and b remains unchanged.
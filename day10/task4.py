import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# PART 1: Generate many vector pairs
# ============================================================

angles = []
dots = []

# Fixed vector pointing along the x-axis
base = np.array([1.0, 0.0])


# Generate vectors from 0° to 180°
for deg in range(0, 181, 5):

    # NumPy trigonometric functions use radians
    rad = np.radians(deg)

    # Create a unit vector at the current angle
    v = np.array([
        np.cos(rad),
        np.sin(rad)
    ])

    # Store the angle
    angles.append(deg)

    # Calculate and store the dot product
    dots.append(base @ v)


# Convert lists to NumPy arrays
angles = np.array(angles)
dots = np.array(dots)


# ============================================================
# PART 2: Plot dot product against angle
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    angles,
    dots,
    marker="o",
    label="Dot product"
)

# Horizontal line at dot product = 0
plt.axhline(
    0,
    linestyle="--",
    label="Dot product = 0"
)

# Vertical line at 90°
plt.axvline(
    90,
    linestyle="--",
    label="90 degrees"
)

plt.xlabel("Angle (degrees)")
plt.ylabel("Dot product")

plt.title("Dot Product vs Angle")

plt.legend()
plt.grid(True)

plt.show()


# ============================================================
# PART 3: Confirm dot product at 90° is approximately zero
# ============================================================

index_90 = np.where(angles == 90)[0][0]

dot_at_90 = dots[index_90]

print("===== 90 DEGREE CHECK =====")

print("Angle:", angles[index_90])
print("Dot product:", dot_at_90)

print(
    "Is dot product approximately zero?",
    np.isclose(dot_at_90, 0)
)


# ============================================================
# PART 4: Three hand-built examples
# ============================================================


# ------------------------------------------------------------
# Example 1: Perpendicular
# ------------------------------------------------------------

a1 = np.array([1.0, 0.0])
b1 = np.array([0.0, 1.0])

dot1 = a1 @ b1

angle1 = np.degrees(
    np.arccos(
        np.clip(
            dot1 / (
                np.linalg.norm(a1)
                * np.linalg.norm(b1)
            ),
            -1,
            1
        )
    )
)


# ------------------------------------------------------------
# Example 2: 45 degrees
# ------------------------------------------------------------

a2 = np.array([1.0, 0.0])

b2 = np.array([
    np.cos(np.radians(45)),
    np.sin(np.radians(45))
])

dot2 = a2 @ b2

angle2 = np.degrees(
    np.arccos(
        np.clip(
            dot2 / (
                np.linalg.norm(a2)
                * np.linalg.norm(b2)
            ),
            -1,
            1
        )
    )
)


# ------------------------------------------------------------
# Example 3: Nearly parallel
# ------------------------------------------------------------

a3 = np.array([1.0, 0.0])

b3 = np.array([
    np.cos(np.radians(10)),
    np.sin(np.radians(10))
])

dot3 = a3 @ b3

angle3 = np.degrees(
    np.arccos(
        np.clip(
            dot3 / (
                np.linalg.norm(a3)
                * np.linalg.norm(b3)
            ),
            -1,
            1
        )
    )
)


# ============================================================
# PART 5: Print results
# ============================================================

print("\n===== THREE HAND-BUILT EXAMPLES =====")

print("\nPerpendicular:")
print("Angle:", angle1, "degrees")
print("Dot product:", dot1)

print("\n45 degrees:")
print("Angle:", angle2, "degrees")
print("Dot product:", dot2)

print("\nNearly parallel:")
print("Angle:", angle3, "degrees")
print("Dot product:", dot3)


# ============================================================
# PART 6: Draw perpendicular vectors
# ============================================================

plt.figure(figsize=(6, 6))

plt.quiver(
    0, 0,
    a1[0], a1[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.quiver(
    0, 0,
    b1[0], b1[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.xlim(-0.2, 1.3)
plt.ylim(-0.2, 1.3)

plt.axhline(0)
plt.axvline(0)

plt.xlabel("X")
plt.ylabel("Y")

plt.title(
    f"Perpendicular (90°), dot product = {dot1:.3f}"
)

plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()


# ============================================================
# PART 7: Draw 45 degree vectors
# ============================================================

plt.figure(figsize=(6, 6))

plt.quiver(
    0, 0,
    a2[0], a2[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.quiver(
    0, 0,
    b2[0], b2[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.xlim(-0.2, 1.3)
plt.ylim(-0.2, 1.3)

plt.axhline(0)
plt.axvline(0)

plt.xlabel("X")
plt.ylabel("Y")

plt.title(
    f"45°, dot product = {dot2:.3f}"
)

plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()


# ============================================================
# PART 8: Draw nearly parallel vectors
# ============================================================

plt.figure(figsize=(6, 6))

plt.quiver(
    0, 0,
    a3[0], a3[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.quiver(
    0, 0,
    b3[0], b3[1],
    angles="xy",
    scale_units="xy",
    scale=1
)

plt.xlim(-0.2, 1.3)
plt.ylim(-0.2, 0.5)

plt.axhline(0)
plt.axvline(0)

plt.xlabel("X")
plt.ylabel("Y")

plt.title(
    f"Nearly parallel (10°), dot product = {dot3:.3f}"
)

plt.grid(True)
plt.gca().set_aspect("equal")

plt.show()
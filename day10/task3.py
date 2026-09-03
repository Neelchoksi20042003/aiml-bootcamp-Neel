import numpy as np


# ---------------------------------------------------------
# Gram-Schmidt Orthogonalisation
# ---------------------------------------------------------

def gram_schmidt(vectors):
    """
    Convert input vectors into an orthonormal basis.

    Dependent vectors are skipped if the remaining
    vector has a very small norm.
    """

    basis = []

    for v in vectors:

        # Work with a floating-point copy
        w = v.astype(float).copy()

        # Remove projections onto all previous basis vectors
        for b in basis:
            w = w - (v @ b) * b

        # Calculate the remaining vector's magnitude
        norm = np.linalg.norm(w)

        # Ignore zero or nearly-zero vectors.
        # A tolerance is used because floating-point calculations
        # may produce tiny values instead of exact zero.
        if norm > 1e-10:
            basis.append(w / norm)

    return np.array(basis)


# =========================================================
# TEST 1: Three independent 3D vectors
# =========================================================

vectors = np.array([
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
], dtype=float)

Q = gram_schmidt(vectors)

print("===== GRAM-SCHMIDT RESULT =====")
print(Q)


# =========================================================
# TEST 2: Prove orthonormality
# =========================================================

identity = Q @ Q.T

print("\n===== Q @ Q.T =====")
print(identity)

print("\nIs Q orthonormal?")
print(np.allclose(identity, np.eye(Q.shape[0]), atol=1e-10))


# =========================================================
# TEST 3: Check same rank
# =========================================================

original_rank = np.linalg.matrix_rank(vectors)
Q_rank = np.linalg.matrix_rank(Q)

print("\n===== RANK CHECK =====")
print("Original rank:", original_rank)
print("Q rank:", Q_rank)

print("Same rank:", original_rank == Q_rank)


# =========================================================
# TEST 4: Dependent vectors
# v3 = v1 + v2
# =========================================================

dependent_vectors = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0]
], dtype=float)

Q_dependent = gram_schmidt(dependent_vectors)

print("\n===== DEPENDENT INPUT =====")
print(Q_dependent)

print("Shape:", Q_dependent.shape)
print("Rank:", np.linalg.matrix_rank(Q_dependent))


# =========================================================
# TEST 5: Compare with NumPy QR
# =========================================================

Q_numpy, R = np.linalg.qr(vectors.T)

# NumPy stores basis vectors as columns.
# Our implementation stores basis vectors as rows.
Q_numpy_rows = Q_numpy.T

print("\n===== NUMPY QR =====")
print(Q_numpy_rows)

print("\nSame basis up to sign?")
print(
    np.allclose(
        np.abs(Q),
        np.abs(Q_numpy_rows),
        atol=1e-10
    )
)
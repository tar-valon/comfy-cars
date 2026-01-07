import numpy as np

# Parameters
m1 = d1 = k1 = 4
m2 = d2 = k2 = 1

# Define matrix A
A = np.array([
    [0, (-k1 - k2)/m1, 0, k2/m1],
    [1, (-d1 - d2)/m1, 0, d2/m1],
    [0, k2/m2, 0, -(k2/m2)],
    [0, d2/m2, 1, -d2/m2]
], dtype=float)

# Compute eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("Eigenvalues:")
print(eigenvalues)

import numpy as np
from numpy.linalg import matrix_rank
import matplotlib.pyplot as plt

###### Assignment 10

# Controllability test

# Equilibrium positions
y1_star = 0.3
y2_star = 0.6

# Parameters
m1 = 1400
d1 = 1000
k1 = 1000
m2 = 100
d2 = 50
k2 = 50

# Matrix A
A = np.array([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-(k1+k2)/m1, k2/m1, -(d1+d2)/m1, d2/m1],
    [k2/m2, -k2/m2, d2/m2, -d2/m2]
])

# Matrix B
B = np.array([[0],[0],[-1/m1],[1/m2]])

# Controllability matrix
Ctr = np.hstack([B, A@B, A@A@B, A@A@A@B])

# The rank of the controllability matrix
rank = matrix_rank(Ctr)
print("rank =", rank)
if rank == 4:
    print("The system is controllable")

# Euler settings
h = 0.01
tend = 20

def simulate(x, A=A):
    t = 0

    T = []
    Y1 = []
    Y2 = []

    while t < tend:
        # Euler step: x = x + h*(A x)
        x = x + h * (A @ x)
        t += h

        T.append(t)
        Y1.append(y1_star + x[0])
        Y2.append(y2_star + x[1])

    return T, Y1, Y2

x0 = np.array([0, -0.2, 0, 0])

T1, Y1a, Y2a = simulate(x0)

plt.figure()
plt.plot(T1, Y1a, label="$y_{*1} + y_1(t)$")
plt.plot(T1, Y2a, label="$y_{*2} + y_2(t)$")

plt.xlabel("t [s]")
plt.ylabel("position [m]")
plt.legend()
plt.show()


# Closed loop system
F = np.array([[22,62,35,108]])
x_prime = A - B @ F

T2, Y1a, Y2a = simulate(x0, x_prime)
plt.figure()
plt.plot(T1, Y1a, label="$y_{*1} + y_1(t)$")
plt.plot(T1, Y2a, label="$y_{*2} + y_2(t)$")

plt.xlabel("t [s]")
plt.ylabel("position [m]")
plt.legend()
plt.show()

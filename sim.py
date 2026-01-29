import numpy as np
import matplotlib.pyplot as plt

###### Assignment 3 and 4
# Change parameters for assignment 3 or 4

# Equilibrium positions
y1_star = 0.3
y2_star = 0.6

# Parameters
m1 = 1400
m2 = 100
d1 = 1000
d2 = 200
k1 = 1000
k2 = 100

# Matrix A
A = np.array([
    [0, (-k1 - k2)/m1, 0, k2/m1],
    [1, (-d1 - d2)/m1, 0, d2/m1],
    [0, k2/m2, 0, -(k2/m2)],
    [0, d2/m2, 1, -d2/m2]
], dtype=float)

# matrix B
B = np.array([k1/m1, d1/m1, 0, 0])

# Euler settings
h = 0.01
tend = 20

def simulate(x):
    t = 0

    T = []
    Y1 = []
    Y2 = []

    while t < tend:
        # Euler step: x = x + h*(A x)
        x = x + h * (A @ x)
        t += h

        T.append(t)
        Y1.append(y1_star + x[1])
        Y2.append(y2_star + x[3])

    return T, Y1, Y2

# Case 1: body initially close to road
x0_1 = np.array([0, -0.2, 0, 0])

# Case 2: chair initially close to body
x0_2 = np.array([0, 0, 0, -0.2])

T1, Y1a, Y2a = simulate(x0_1)
T2, Y1b, Y2b = simulate(x0_2)

plt.figure()
plt.plot(T1, Y1a, label="$y_{*1} + y_1(t)$ Body")
plt.plot(T1, Y2a, label="$y_{*2} + y_2(t)$ Chair")

plt.xlabel("t [s]")
plt.ylabel("position [m]")
plt.legend()
plt.show()

plt.figure()
plt.plot(T2, Y1a, label="$y_{*1} + y_1(t)$ Body")
plt.plot(T2, Y2a, label="$y_{*2} + y_2(t)$ Chair")

plt.xlabel("t [s]")
plt.ylabel("position [m]")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

###### Assignment 5

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


# input variations
def u(t):
    return 0.0 if t < 1.0 else 1.0


# Euler settings
h = 0.01
tend = 20

def simulate(d1):
    t = 0

    # Matrix A
    A = np.array([
        [0, (-k1 - k2)/m1, 0, k2/m1],
        [1, (-d1 - d2)/m1, 0, d2/m1],
        [0, k2/m2, 0, -(k2/m2)],
        [0, d2/m2, 1, -d2/m2]
    ], dtype=float)

    # matrix B
    B = np.array([k1/m1, d1/m1, 0, 0])

    # Initial state
    x = np.array([0, 0, 0, 0], dtype=float)

    T = []
    Y1 = []

    while t < tend:
        # Euler step
        x = x + h * (A @ x + B * u(t))
        t += h

        T.append(t)
        Y1.append(x[1])

    return T, Y1


plt.figure()

# D1 values
d1_values = np.arange(250, 2001, 250)

for d1 in d1_values:
    T, Y1 = simulate(d1)
    plt.plot(T, Y1, label=f"$d_1 =$ {d1}")

plt.xlabel("$t$ [s]")
plt.ylabel("$y_1(t)$ [m]")
plt.legend(loc='best', fontsize='small')
plt.show()

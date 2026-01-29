import numpy as np
import matplotlib.pyplot as plt

###### Assignment 9

# Equilibrium positions
y1_star = 0.3
y2_star = 0.6

# Parameters
m1 = 1400
d1 = 1000
k1 = 1000
m2 = 100
d2 = 200
k2 = 100

# Single bump
z_on  = 5.0
z_off = 9.5
h_bump = 0.10
l_bump = z_off - z_on

def u(z):
    if z < z_on or z > z_off:
        return 0.0
    arg = np.pi * (z - z_on) / l_bump
    return h_bump * np.sin(arg)

v = 3.0

# Matrix A
A = np.array([
    [0, (-k1 - k2)/m1, 0, k2/m1],
    [1, (-d1 - d2)/m1, 0, d2/m1],
    [0, k2/m2, 0, -k2/m2],
    [0, d2/m2, 1, -d2/m2]
], dtype=float)

# Matrix B
B = np.array([k1/m1, d1/m1, 0, 0])

# Matrix C
C = np.array([
                  [0, 1, 0, 0],
                  [0, 0, 0, 1]
              ], dtype=float)

# Euler settings
h = 0.01
tend = 20.0
x = np.zeros(4)

t_list = []
y1_dot_list = []
y2_dot_list = []

t = 0.0
while t < tend:
    ut = u(v * t)

    # Euler step
    x_dot = A @ x + B * ut
    x = x + h * x_dot
    t = t + h

    y1_dot = C[0] @ (A @ x + B * ut)
    y2_dot = C[1] @ (A @ x + B * ut)

    t_list.append(t)
    y1_dot_list.append(y1_dot)
    y2_dot_list.append(y2_dot)


plt.figure()
plt.plot(t_list, y1_dot_list, label='$y_1^{\prime}(t)$')
plt.plot(t_list, y2_dot_list, label='$y_2^{\prime}(t)$')
plt.xlabel('t [s]')
plt.ylabel('speed $y^{\prime}(t)$ $[ms^{-1}]$')
plt.legend()
plt.show()

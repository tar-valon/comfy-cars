import numpy as np
import matplotlib.pyplot as plt

###### Assignment 6

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



def u(z):
    # Bump sinusoid values
    z_on  = 5.0
    z_off = 9.5
    h_bump = 0.10
    l_bump = z_off - z_on

    if z < z_on or z > z_off:
        return 0.0
    arg = np.pi * (z - z_on) / l_bump
    return h_bump * np.sin(arg)

v = 3.0

# matrix A
A = np.array([
    [0, (-k1 - k2)/m1, 0, k2/m1],
    [1, (-d1 - d2)/m1, 0, d2/m1],
    [0, k2/m2, 0, -k2/m2],
    [0, d2/m2, 1, -d2/m2]
], dtype=float)

# Matrix B
B = np.array([k1/m1, d1/m1, 0, 0])

# Euler settings
h = 0.01
tend = 20.0
x = np.zeros(4)

t_list = []
u_list = []
y1_list = []
y2_list = []
rel_list = []

t = 0.0
while t < tend:
    ut = u(v * t)
    t_list.append(t)
    u_list.append(ut)
    y1_list.append(y1_star + x[0])
    y2_list.append(y2_star + x[2])
    rel_list.append(x[0] - ut)

    # Euler step
    x_dot = A @ x + B * ut
    x = x + h * x_dot
    t = t + h

plt.figure()
plt.plot(t_list, u_list, label='u(t)')
plt.plot(t_list, y1_list, label='y1*(t)')
plt.plot(t_list, y2_list, label='y2*(t)')
plt.plot(t_list, rel_list, label='y1(t) - u(t)')
plt.xlabel('time [s]')
plt.ylabel('position [m]')
plt.legend()
plt.show()

max_rel = max([abs(val) for val in rel_list])
print('Maximum |y1(t) - u(t)| =', max_rel)

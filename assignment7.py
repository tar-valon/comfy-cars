import numpy as np
import matplotlib.pyplot as plt

###### Assignment 7
# NOTE: change value of s for second graph

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

# gap between bumps
s = 0


def u(z):
    # Bump sinusoid values
    z_on1  = 5.0
    z_off1 = 9.5
    h_bump = 0.10
    l_bump = z_off1 - z_on1

    z_on2  = z_off1 + s
    z_off2 = z_on2 + l_bump

    if z_on1 <= z <= z_off1:
        arg = np.pi * (z - z_on1) / l_bump
        return h_bump * np.sin(arg)
    # second bump
    if z_on2 <= z <= z_off2:
        arg = np.pi * (z - z_on2) / l_bump
        return h_bump * np.sin(arg)
    return 0.0

v = 3.0

# Matrix A
A = np.array([
    [0, (-k1 - k2)/m1, 0, k2/m1],
    [1, (-d1 - d2)/m1, 0, d2/m1],
    [0, k2/m2, 0, -k2/m2],
    [0, d2/m2, 1, -d2/m2]
], dtype=float)

# matrix B
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
    # Euler step
    x = x + h * (A @ x + B * ut)
    t += h
    t_list.append(t)
    u_list.append(ut)
    y1_list.append(y1_star + x[1])
    y2_list.append(y2_star + x[3])
    rel_list.append(x[1] - ut)

plt.figure()
plt.plot(t_list, u_list, label='$u(t)$')
plt.plot(t_list, y1_list, label='$y_{*1} + y_1(t)$')
plt.plot(t_list, y2_list, label='$y_{*2} + y_2(t)$')
plt.plot(t_list, rel_list, label='$y_1(t) - u(t)$')
plt.xlabel('t [s]')
plt.ylabel('position [m]')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


plt.show()


max_rel = max([abs(val) for val in rel_list])
print('Maximum |y1(t) - u(t)| =', max_rel)

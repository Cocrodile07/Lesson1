import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def dU_dx(U, x):
    C = 0.0025
    K = 39.75 #Spring constant (arbitrary unit)
    M = 0.260 #Kg
    F = 0.26*9.8 #The weight acting on the
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], ((1/M)*(-C*U[1] - K*U[0]+ F))]


U0 = [0, 0]
xs = np.linspace(0, 30, 90000)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]

plt.xlabel("t")
plt.ylabel("y")
plt.title("Damped harmonic oscillator")
plt.plot(xs,ys)
plt.show()

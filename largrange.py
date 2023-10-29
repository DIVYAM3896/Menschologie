
# Calculate L1 and L2 Lagrange Points

import matplotlib.pyplot as plt
import numpy as np

G = 6.67e-11 #N*m^2/kg^2
Me = 5.972e24 #kg
Ms = 1.989e30

r = 1.496e11

g1 = plt.plot(xtitle="h [m]", ytitle = "stuff")



h = 5e8
dh = 1e8

while h < 3e9:
    lhs = G*Ms/(r+h)**2 + G*Me/h**2
    rhs = G*Ms*(r+h)/r**3
    h = h+dh
    print(lhs)
    print(rhs)
    print(h)

    plt.plot(h,lhs)
    plt.plot(h,rhs)    
    plt.show()
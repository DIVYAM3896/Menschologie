# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:27:34 2021

@author: Divyam
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy as s

# Initialization

tstart=0
tstop=25
increment=1
x0= np.arange(1,100,1)
t=np.arange(tstart,tstop+1,increment)
print(t)

# function dx/dt

def mydiff(x,t):
    T=5
    a=-1/T
    dxdt=a**2*(x)
    return dxdt

# solve ode

x = odeint(mydiff, x0, t)
print(x)

# plot the output

plt.plot(t,x)
plt.grid()
plt.show()


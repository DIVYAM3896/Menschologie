# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 15:01:03 2021

@author: Divyam
"""
# birth rate - bx
# death rate - px^2
# equation - dx/dt= b*x-p*x^2
# b - 1/hour
# p - 0.5/hour

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# initialize
b=1
p=0.5
tstart = 0
tstop = 1
x0 = 100    # means that a t=0 there are 100 bacteria
t=np.arange(tstart,tstop,0.1)

# def function

def bacteriadiff(x,t):
    dxdt=b*x-p*x**2
    return dxdt

# solve ODE

x=odeint(bacteriadiff,x0,t)

#plot 

plt.plot(x,t)
plt.show()
    
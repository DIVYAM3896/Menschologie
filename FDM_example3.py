# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:40:27 2022

@author: Divyam
"""
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
df = lambda x : 0.5*x**4 - 0.6*x**2 + 0.1
h = 0.001
x = np.linspace(-1,1,100)
plt.plot(x,df(x),'-k')


# forward differences
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
plt.plot(x,dff1,'--b')


# backward differences
dbff1 = (f(x) - f(x-h))/h
dbff2 = (f(x) - 2*f(x-h) + f(x-2*h))/h**2
plt.plot(x,dbff1,'-.r')


# central difference
dcff1 = (f(x+h) - f(x-h))/(2*h)
dcff2 = (f(x+h) - 2*f(x) + f(x-h))/h**2
plt.plot(x,dcff1,'-g')

# plot
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["theoretical", "forward", "backward", "central"])
plt.grid()
plt.show()



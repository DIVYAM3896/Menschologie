# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:28:30 2022

@author: Divyam
"""
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
h = 0.001
x = np.linspace(-1,1,100)

# forward differences
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2


# backward differences
dbff1 = (f(x) - f(x-h))/h
dbff2 = (f(x) - 2*f(x-h) + f(x-2*h))/h**2


# central difference
dcff1 = (f(x+h) - f(x-h))/(2*h)
dcff2 = (f(x+h) - 2*f(x) + f(x-h))/h**2

plt.plot(x,f(x),'-k', x,dff1,'--b', x,dff2,'-.r')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["f(X)", "f'(x)", "f''(x)"])
plt.grid()
plt.show()

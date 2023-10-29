# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:21:05 2022

@author: Divyam
"""
# finite difference method
f = lambda x: 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
x = 0.1
h = 0.001

df1 = 0.09405
df2 = -0.118

print("\t f'(x)\t\t err\t\t f''(x)\t\t err")   # \t tab specifiers: used to give spaces in statements

# forward differences
dff1 = (f(x+h) - f(x))/h
dff2 = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
print("FFD %f\t% f\t% f\t% f" % (dff1, dff1-df1, dff2, dff2-df2))

# backward differences
dbff1 = (f(x) - f(x-h))/h
dbff2 = (f(x) - 2*f(x-h) + f(x-2*h))/h**2
print("BFD %f\t% f\t% f\t% f" % (dbff1, dbff1-df1, dbff2, dbff2-df2))

# central difference
dcff1 = (f(x+h) - f(x-h))/(2*h)
dcff2 = (f(x+h) - 2*f(x) + f(x-h))/h**2
print("CFD %f\t% f\t% f\t% f" % (dcff1, dcff1-df1, dcff2, dcff2-df2))

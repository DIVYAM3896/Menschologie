# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:54:09 2022

@author: Divyam
"""
# 2D - Plotting Scalar and Vector Fields with Python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 15, 1)
y = np.arange(1, 15, 1)
z = np.arange(1, 15, 1)
X, Y, Z = np.meshgrid(x,y,z);
W = np.cos(np.pi*(np.sqrt(np.square(X)+np.square(Y)+np.square(Z))))
print(W)
plt.grid()
plt.contour(X, Y,W, cmap='gist_rainbow_r')
plt.show()

## errors
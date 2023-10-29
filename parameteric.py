import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, np.pi, 1, dtype=float)
x = np.sin(t)+0.5*np.sin(5*t)+0.25*np.cos(2.3*t)
y = np.cos(t)+0.5*np.cos(5*t)+0.25*np.sin(2.3*t)
X,Y = np.meshgrid(x,y);
plt.grid()
plt.plot(X,Y,t)
plt.show()



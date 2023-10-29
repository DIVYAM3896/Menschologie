#%% 2-d vector fields example 1
import numpy as np
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

u = 1
v = -1

u = x/np.sqrt(x**2 + y**2)
v = x/np.sqrt(x**2 + y**2)

plt.quiver(x,y,u,v)
plt.grid()
plt.show()

#%% 2-d vector fields example 2

import numpy as np
import matplotlib.pyplot as plt


x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

u = x/np.sqrt(x**2 + y**2)
v = y/np.sqrt(x**2 + y**2)

plt.quiver(x,y,u,v,color='red')
plt.grid()
plt.show()
#%% 3-d vector fields example 2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline


fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.5, color = 'blue')

plt.show()


#%% 3-d vector fields example 3 just for fun
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
ax = fig.gca(projection='3d')


x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

alpha = np.random.rand()
beta = np.random.rand()
gamma = np.random.rand()


u = np.sin(alpha)
v = np.cos(beta)
w = np.sin(alpha)*np.cos(gamma)

ax.quiver(x, y, z, u, v, w, length=0.1, color = 'blue')

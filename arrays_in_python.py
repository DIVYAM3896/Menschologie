# create arrays in python using numpy
import numpy as np

# create one dimensional array
d_1 = np.array([1, 2, 3, 4])
print(d_1)
print(d_1.ndim)

# create two dimensional array
d_2 = np.array([[1, 2], [3, 4]])
print(d_2)
print(d_2.ndim)

# Arrays filled with constant values
d_3 = np.zeros((2, 3))  # here (2,3) is the size of the array
print(d_3)
print(d_3.ndim)

d_4 = np.ones((5, 5), dtype=np.float_)  # here we can mention data type , it is optional
print(d_4)
print(d_4.ndim)


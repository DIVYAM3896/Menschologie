import numpy as np
data = np.array([[1, 2],[3, 4],[5, 6]])
print(type(data))
print(data)
print(data.ndim)
print(data.shape)
print(data.size)
print(data.dtype)
print(data.nbytes)

d1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.complex128)
# here we can pre define the data type
# and cannot change data type if pre-defined
print(d1)

# to change the data type we can use (np.asarray)
np.asarray(data, np.str_)
print(data)

# change data type using astype
data.astype(np.int_)
print(data)

# promotion of data type while computing

d2 = np.array([1, 2, 5], dtype=np.float_)   # data type is float
d3 = np.array([6, 7, 8], dtype=np.complex_)  # data type is complex
d4 = d2+d3
print(d4)   # data type is promoted to complex
print(d4.dtype)

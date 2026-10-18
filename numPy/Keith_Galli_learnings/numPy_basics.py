import numpy as np

a = np.array([1,2,3])

print(a)

b = np.array([[9.0,8.0,7.0], [6.0,5.0,4.0]])

print(b)

#get dimension of arrays

print(a.ndim)
print(b.ndim)

#Get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#change dtype
a = np.array([1,2,3], dtype = 'int16')
print(a.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#get total size - number of elements
print(a.size)
print(b.size)

#get total array size in terms of bytes
print(a.size * a.itemsize)
print(a.nbytes)
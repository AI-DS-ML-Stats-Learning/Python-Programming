import numpy as np

a = np.array([1,2,3,4])
print(a)

#nmpy does element wise operation
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

b = np.array([1,0,1,0])

print(a+b)

#take sin of all values
print(np.sin(a))
print(np.cos(a))
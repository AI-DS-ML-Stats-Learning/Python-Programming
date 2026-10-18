import numpy as np
a = np.array([1,2,3])

b = a #shallow copy

b[0] = 100

print(b)
print(a)


b = a.copy() #deep copy, does not changes the parent array
b[0] = 23

print(a)
print(b)
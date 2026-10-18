import numpy as np
# all 0s matrix

print(np.zeros(5))
print(np.zeros((2,3))) #2-dimensional
print(np.zeros((2,3,3))) #3-dimensional
print(np.zeros((2,3,2,2))) #4-dimensional

# all 1s matrix

print(np.ones(4))
print(np.ones((2,4)))
print(np.ones((4,2,1)))

# any other number matrix
print(np.full((2,2), 99, dtype = 'float32'))

# any other number full_like
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a.shape)
print(np.full_like(a.shape,4))
print(np.full(a.shape,4))

# random decimal numbers
print(np.random.rand(4,2))
print(np.random.rand(4,2,3))
print(np.random.random_sample(a.shape))

# random integar values
print(np.random.randint(7, size=(3,3))) #by default starts at 1 and takes the input value as end value (exclusive)
print(np.random.randint(4,7, size=(3,3))) #added start and end value

# the indentity matrix
print(np.identity(5)) #needs only 1 parameter as identity is by default a square matrix

#repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis = 0)
print(r1)
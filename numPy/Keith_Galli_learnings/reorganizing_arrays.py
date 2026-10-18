import numpy as np

before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)

after = before.reshape((4,2))
print(after)

after = before.reshape((2,2,2))
print(after)

#vertically stacking vectors/matrices
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

#note: for vertical stacking, the col count should be same
print(np.vstack([v1,v2,v2]))

#horizontal stacking vectors/matrices
h1 = np.ones((2,3))
h2 = np.zeros((2,4))

print(h1)
print(h2)

#note: for horizontal stacking, the row count should be same

print(np.hstack([h1,h2]))
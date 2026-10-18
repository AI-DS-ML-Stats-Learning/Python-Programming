#indexing a matrix

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
# 26 27 28 29 30

# 1. index 
# 11 12
# 16 17

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]).reshape(6,5)
arr = np.arange(1, 31).reshape(6, 5) #optimized way
print(arr)

print(arr[2:4,0:2])

# 2. index
# 2, 8, 14, 20

print(arr[0:4,1:5])
print("\n")

print(arr[0:4,1:5][0][0])
print(arr[0:4,1:5][1][1])
print(arr[0:4,1:5][2][2])
print(arr[0:4,1:5][3][3])
print("\n")

slice = arr[0:4,1:5]
for i in range(4):
    print(slice[i,i])

print("\n")
print(arr[[0,1,2,3],[1,2,3,4]])


# 3. index
# 4, 5, 24, 25, 29, 30

print(arr[[0,4,5],3:])

print("\n")
#np.ix_ tells NumPy to take every combination of these rows and these columns.
print(arr[np.ix_([0,4,5],[3,4])])
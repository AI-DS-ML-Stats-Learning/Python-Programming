import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a.shape)
print(a)

#get a specific element - [row index, col index]

##fetch 13 from array a
print(a[1,5]) #positive notation
print(a[-1,-2]) #negative notation

# get a specific row
print(a[0, :])
print(a[0, ])

# get a specific column
print(a[:, 2])

# getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2]) #endindex is actually exclusive of the reference

# update an index element

a[1,5] = 20
print(a)

a[:,2] = 5 #update an entire column 
print(a)

# 3-D Array Example

b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)
##get specific element ion 3d array (work outside in)
print(b[0,1,1])
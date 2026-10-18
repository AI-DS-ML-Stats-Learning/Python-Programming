import numpy as np

stats = np.array([[1,2,3], [4,5,6]])
print(stats)

# min max
print(np.min(stats)) # min value in the array
print(np.min(stats, axis=0)) #min value in each col 
print(np.min(stats, axis=1)) #min value in each row
print(np.max(stats))
print(np.max(stats, axis = 0))
print(np.max(stats, axis = 1))
print(np.sum(stats))
print(np.sum(stats, axis = 0)) #col wise sum
print(np.sum(stats, axis = 1)) #row wise sum
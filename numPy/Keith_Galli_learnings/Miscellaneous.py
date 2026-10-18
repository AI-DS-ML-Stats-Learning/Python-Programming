# Load data from a file

import numpy as np

data_file = np.genfromtxt('data.txt', delimiter = ',')
data_file = data_file.astype(np.int32)
print(data_file)

## Boolean masking and Advanced indexing

print(data_file > 50)
print(data_file[data_file > 50])

#check if any values in each column is greater than 50
print(np.any(data_file > 50, axis = 0))

#check if all values in each column is greater than 50
print(np.all(data_file > 50, axis = 0))

#values greater than 50 and less than 100
print((data_file>50) & (data_file <100))
print(data_file[(data_file>50) & (data_file <100)]) #print values

#values not greater than 50 and less than 100
print(~((data_file>50) & (data_file <100)))

## You can index with a list in NumPY
a = np.array([1,2,3,4,5,6,7,8,9])

print(a[[1,2,8]])
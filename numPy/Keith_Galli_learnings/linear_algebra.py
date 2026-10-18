import numpy as np

a = np.ones((2,3))
b = np.full((3,2),2)

print(a)
print(b)

#concept of linear algebra = col of 1st matrix = row of second matrix

matrix_multiplied = np.matmul(a,b)
print(matrix_multiplied)

# find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# what all we can do with matrices and linear algebra
# Determinant
# Trace
# Singular Vector Decomposition
# Eigen-values
# Matrix Norm
# Inverse
# etc
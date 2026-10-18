import numpy as np

# 1 1 1 1 1 -> row = 0
# 1 0 0 0 1 -> row = 1
# 1 0 9 0 1 -> row = 2
# 1 0 0 0 1 -> row = 3
# 1 1 1 1 1 -> row = 4

arr = np.ones((5,5), dtype = np.int16)
# arr[1:4,1:4] = 0
arr[1:-1,1:-1] = 0
arr[2,2] = 9

print(arr)

# inner = np.zeros((3,3), dtype=np.int16)
# inner[1,1] = 9
# arr = np.pad(inner, pad_width=1, constant_values=1)
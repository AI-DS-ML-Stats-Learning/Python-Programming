import numpy as np

# Create your original image: Initialize a 5 x 5 matrix filled entirely with the integer 255 
# (representing white pixels). 
# Set the dtype explicitly to np.uint8.
new_arr = np.full((5,5), 255, dtype = np.uint8)

# print(new_arr)  

# Slice-edit the center: Change the middle 3 x 3 region of this matrix to the value 0 (representing a black box) using 
# a single slicing command (e.g., matrix[row_start:row_end, col_start:col_end] = 0). No for loops allowed!

new_arr[1:4, 1:4] = 0
# print(new_arr)

# Verify the Copy Trap:
# Create a shallow reference to your matrix: shallow_ref = matrix.
# Create a true copy of your matrix: deep_copy = matrix.copy().
# Change the very first pixel (index [0, 0]) of shallow_ref to 128 (representing gray).
# Change the very last pixel (index [4, 4]) of deep_copy to 50 (representing dark gray).
shallow_ref = new_arr
deep_copy = new_arr.copy()

shallow_ref[0,0] = 128
deep_copy[4,4] = 50

print(new_arr, '\n')
print(shallow_ref, '\n')
print(deep_copy)
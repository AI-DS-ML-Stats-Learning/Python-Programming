# Write a Python script from scratch that implements these steps:
#   Initialize a 3D Tensor:
# 	    Generate a 3D NumPy array of shape (3, 4, 4) containing sequential integers from 1 to 48 
# 		(Hint: Use np.arange(1, 49).
# 			reshape(3, 4, 4)).
# 	Examine Metadata:
    # 	Print your tensor's .shape and .strides. (Take a second to think about what the three values in .strides 
    #   actually represent!).
# 	Surgically Slice the Tensor:
#       Extract the middle 2 x 2 region of the second matrix (index 1).
    # 	Change all four values of this sliced region to -99 in a single command.
    # Verify the View Effect:
        # Print your entire modified 3D tensor to prove that editing your sliced view successfully mutated the 
        # parent tensor in place.
    # Targeted Coordinates with Negative Indexing:
        # Print the value of the very last element of the last row of the last matrix using strictly negative indices.

import numpy as np

#Initialize a 3D Tensor
tensor_arr = np.arange(1,49).reshape(3,4,4)

#Examine Metadata
print(tensor_arr.shape)
print(tensor_arr.strides)
# (128, 32, 8) -> 128 means 128 bytes to get to the next block or next 2D array within the tensor 
# and remainng 32 means, 32 bytes to move to next row and 4 bytes to next column

# Surgically Slice the Tensor
tensor_arr[1,1:3, 1:3] = -99

# Verify the View Effect:
print(tensor_arr, '\n')
# print(sliced_tensor)

# Targeted Coordinates with Negative Indexing
print(tensor_arr[-1, -1, -1])


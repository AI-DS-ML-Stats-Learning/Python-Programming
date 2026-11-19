 #### **Instructions:**
# Write a Python script from scratch that implements these steps:

# 1. **Create a Synthetic Dataset:**
#    * Generate a 5 X 3 matrix containing random integers between `10` and `100` 
#       (Use `np.random.randint(10, 101, size=(5, 3))`). This represents 5 sample data points across 3 numerical features [3].
# 2. **Calculate Feature Column Statistics:**
#    * Compute the **mean of each column** across samples (Hint: Use `mean_vector = dataset.mean(axis=0)`). 
#       Confirm its shape is `(3,)` [3].
#    * Compute the **standard deviation of each column** (Hint: Use `std_vector = dataset.std(axis=0)`). 
#       Confirm its shape is `(3,)` [3].
# 3. **Standardize using Broadcasting (No Loops!):**
#    * Perform Z-score normalization by subtracting `mean_vector` from `dataset` and dividing by `std_vector` 
#       in a single line: `normalized_dataset = (dataset - mean_vector) / std_vector` [3].
# 4. **Verify the Broadcaster Output:**
#    * Compute the mean of your `normalized_dataset` along `axis=0` to verify that all column means are 
#         now effectively `0` (or extremely close to 0 due to floating-point representation).
#    * Print `dataset.shape`, `mean_vector.shape`, and the final `normalized_dataset`.

import numpy as np
matrix = np.random.randint(10,101, size = (5,3))
# matrix = np.arange(10, 100).reshape(5,3)
print(matrix)

mean_vector = matrix.mean(axis=0)
std_vector = matrix.std(axis=0)
print(mean_vector)
print(std_vector)
normalized_dataset = (matrix - mean_vector)/std_vector
print(normalized_dataset)
print(normalized_dataset.mean(axis=0))
print(matrix.shape)
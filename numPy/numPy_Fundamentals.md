2. Why is array.shape not callable (array.shape())?

This is a fundamental rule of Python Object-Oriented Programming (OOP) and is highly consistent across NumPy.
In Python OOP, objects have two types of members:
	Attributes (Properties): These are raw variables stored inside the object's header. Since they are pre-calculated variables, you do not use parentheses () to get them.
		Examples: tensor_arr.shape, tensor_arr.strides, tensor_arr.dtype, tensor_arr.nbytes.
	
	Methods (Actions): These are functions defined inside the class that perform calculations or transformations. Because they represent actions, they must be called using parentheses ().
		Examples: tensor_arr.copy(), tensor_arr.reshape(), tensor_arr.mean().

How to tell the difference instantly:
	If you are reading static metadata about the array (its size, memory, type, dimensions) -> Attribute (No parentheses).
	If you are forcing the array to do something (copy, reshape, calculate a sum, save to a file) -> Method (Requires parentheses ()).


### 1. Array Generation & Metadata

# Sequence generation
arr_1d = np.arange(1, 11)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_step = np.arange(0, 10, 2)     # [0, 2, 4, 6, 8] (start, stop, step)

# Core Metadata Attributes (No parenthesis!)
dims    = arr_1d.ndim              # Returns integer (number of dimensions)
shape   = arr_1d.shape             # Returns tuple of dimensions
strides = arr_1d.strides           # Returns tuple of stride steps in bytes
dtype   = arr_1d.dtype             # Returns data type (e.g., int64, float32)
bytes_szize = arr_1d.nbytes        # Returns total memory consumed in RAM

2. Surgical Indexing & Slicing Syntax
Assuming a 2D matrix of shape (5, 5):
matrix = np.arange(25).reshape(5, 5)

# Element access (Row 2, Column 3) - Fast O(1)
val = matrix[2, 3]

# Sub-matrix slice (Rows 1 to 3, Columns 1 to 3) - Returns a VIEW
sub_grid = matrix[1:4, 1:4]

# Column/Row Extraction
entire_row_two = matrix[2, :]      # Get index-2 row
entire_col_three = matrix[:, 3]    # Get index-3 column

# Negative Indexing & Steps
bottom_right_pixel = matrix[-1, -1] # Last row, last column
every_second_row = matrix[::2, :]   # Slices matrix stepping by 2 rows
3. 3D Tensor Navigation (depth, rows, cols)
Assuming a 3D tensor of shape (3, 4, 4):
tensor = np.arange(48).reshape(3, 4, 4)

# Extract first 2D matrix page
first_page = tensor[0, :, :]

# Access single deep element (Last page, 2nd row, 3rd column)
deep_val = tensor[-1, 1, 2]
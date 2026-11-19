Section 1: Concept Clearance & Logical Reasoning
    Concept 1: Why NumPy Slicing is Unique (The "View" Philosophy)
        In standard Python, if you slice a list:
            py_list = [1, 2, 3, 4, 5]
            sub_list = py_list[0:3]  # [1, 2, 3]
            sub_list[0] = 99
            # py_list is still [1, 2, 3, 4, 5] (Slicing created a new list)
        
        In NumPy, slicing does NOT create a copy of the data. It returns a "View" of the original array.
            np_arr = np.array([1, 2, 3, 4, 5])
            view_arr = np_arr[0:3]
            view_arr[0] = 99
            # np_arr is now [99, 2, 3, 4, 5]!

    Why does NumPy do this? 
        1. Slicing a standard list requires copying elements to a new memory address (O(N) time complexity operation). If you are working with a 10 GB dataset of neural network activations, copying memory every time you take a slice would crash your computer and make computations incredibly slow.
        2. By returning a View, NumPy simply creates a tiny metadata wrapper that points to a specific offset in your existing contiguous RAM block. This makes slicing an instant, O(N) memory-safe operation.

    Concept 2: Multidimensional Indexing ([row, col] vs [row][col])
    
        When accessing a 2D matrix element:
            The Slow Python Way: matrix[row][col]
                Why it's slow: matrix[row] runs first, creating a temporary row array in memory, and then [col] indexes into that temporary array.
            
            The Fast NumPy Way: matrix[row, col]
                Why it's fast: NumPy uses its stride metadata to calculate the exact single 1D memory address of that element instantly and fetches it directly from RAM in a single step.
            
    Concept 3: Navigating 3D Arrays (Working Outside-In)
        A 3D array (or 3D tensor) has three dimensions: (depth/matrices, rows, columns).
        Visualize a 3D array as a book:
            The first index selects the page (which 2D matrix you want).The second index selects the row on that page.
            The third index selects the column in that row.
            Accessing tensor[0] returns the entire first 2D matrix. Accessing tensor[0, 1, 2] returns the element in the 1st matrix, 2nd row, 3rd column.
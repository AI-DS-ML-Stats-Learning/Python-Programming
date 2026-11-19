Section 1: Concept Clearance & Logical Reasoning
    Concept 1: Programmatic Array Initialization
        The Need: When training an AI model, you cannot manually write a 2D list. You need to instantly allocate a matrix of weights.
        
        The Methods:
            np.zeros((rows, cols)) allocates a matrix of all zeros.
            np.ones((rows, cols)) allocates a matrix of all ones.
            np.full((rows, cols), value) allocates a matrix filled entirely with a custom value.
        
        Logical Reasoning: Why do we specify dtype=np.uint8 for images?
            "Unsigned 8-bit Integer" (uint8) uses exactly 1 byte (8 bits) of memory per number and can store values from 0 to 255.
            Standard digital image pixels are strictly integers in the 0 (pure black) to 255 (pure white) range.
            By using uint8, we use 1/8th of the memory of NumPy’s default int64 (8 bytes per number). This prevents Out-Of-Memory (OOM) errors when loading large datasets of images into a model.
    
    
    Concept 2: The Copy Trap (Reference vs. View vs. True Copy)
        When you assign or manipulate arrays in NumPy, they behave very differently depending on how you write your code:
        
        Reference (Shallow Assignment): B = A
            What it does: Creates a new label B pointing to the exact same wrapper and memory buffer as A.
            The Trap: Modifying B directly modifies A.

        View (Slicing): B = A[0:2, 0:2]
            What it does: Creates a new Python wrapper object with its own metadata (shape, strides), but shares the exact same raw memory buffer as the original array A.
            The Trap: Slices in NumPy are views, not copies. If you modify a slice of an array, you silently modify the original parent array!
        
        True Copy: B = A.copy()
            What it does: Allocates a brand-new, independent contiguous block of RAM and duplicates all data.
            The Benefit: B and A are completely disconnected. Modifying B has zero effect on A.
            
Section 2: Clean Scripts for Your Markdown (numpy_prep.md)
Here are two highly clean, self-contained scripts. You can run these in VS Code to see the outputs, and then paste them directly into your markdown notes file.
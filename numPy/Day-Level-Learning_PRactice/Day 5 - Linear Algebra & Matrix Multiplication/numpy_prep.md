# Day 5: Linear Algebra & Matrix Operations

## 1. Element-wise (`*`) vs. Matrix Multiplication (`@`)

- **Element-wise (`A * B`):** Multiplies matching coordinates. Requires identical or broadcastable shapes.
- **Dot Product / Matrix Multiplication (`A @ B` or `np.matmul(A, B)`):** Performs row-by-column inner products.
- **Dimensional Alignment Rule:** $(M \times N) @ (N \times P) \rightarrow (M \times P)$. Inner dimensions must match!

## 2. Transposition (`.T`)

- Swaps axes (e.g., shape $(5, 3) \rightarrow (3, 5)$).
- **Zero-Copy Optimization:** Computes in $\mathcal{O}(1)$ time by swapping stride values in the array wrapper.

```python
import numpy as np

# Matrix multiplication alignment
X = np.ones((5, 3))       # Shape (5, 3)
W = np.ones((3, 4))       # Shape (3, 4)

# Forward pass calculation
Y = X @ W                 # Resulting shape: (5, 4)
```
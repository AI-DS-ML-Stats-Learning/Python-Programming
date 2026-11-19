"""
The Scenario:
You are building the forward pass of a simple Neural Network dense layer
for a batch of input samples.

Your Task:
1. Inputs (X): Create a matrix representing a batch of 4 samples, where each
   sample has 5 feature values. Fill this matrix with sequential numbers
   starting from 1.
2. Weights (W): Create a weight matrix representing 3 output neurons, where
   each neuron has 5 incoming weights. Initialize this matrix with random numbers.
3. The Dimension Mismatch Problem:
   - Try to multiply X and W directly using `@`. Notice why Python/NumPy throws an error!
   - Use transposition (`.T`) on the weight matrix so that the inner dimensions
     align correctly according to linear algebra rules.
4. Biases (b): Create a 1D bias vector containing 3 constant values (e.g., [0.1, 0.2, 0.3]).
5. Forward Pass Calculation:
   - Compute the final output matrix Y = (X @ W.T) + b
6. Output Inspection:
   - Print the resulting shape of Y.
   - Confirm it matches your expected batch size and neuron count!
"""

import numpy as np

arr = np.arange(1,21).reshape(4,5)

weight_matrix = np.random.random((3,5))
b = np.array([0.1, 0.2, 0.3])
X = (arr @ weight_matrix.T) +b

print(weight_matrix.T)
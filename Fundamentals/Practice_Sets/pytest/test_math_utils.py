from sqrt_func import calculate_square_root

# Your Task: Write a Python file named test_math_utils.py containing two test functions:

# test_valid_square_root(): Asserts that calculate_square_root(9) returns 3.0.
# test_negative_square_root_raises_error(): Uses pytest.raises(ValueError) 
# to verify that calling calculate_square_root(-9) correctly throws a ValueError.

import pytest

def test_valid_square_root():
    assert calculate_square_root(9) == 4

def test_negative_square_root_raises_error():
    with pytest.raises(ValueError):
        calculate_square_root(-9)

# test_valid_square_root()

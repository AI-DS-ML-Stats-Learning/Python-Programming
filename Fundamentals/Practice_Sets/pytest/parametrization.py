def is_even(n):
    return n % 2 == 0

# We want to test it with 4 different cases:

# 2 should return True
# 3 should return False
# 0 should return True
# -4 should return True
# Instead of writing 4 separate test functions, we will write one test function that runs 4 times with different inputs 
# using Pytest's @pytest.mark.parametrize decorator.

# Your Task: Complete the template below to test all 4 cases:

import pytest

# 1. Fill in the list of test cases (each case is a tuple: (input_number, expected_boolean))
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True)
])
def test_is_even(number, expected):
    # 2. Write the assert statement to check if is_even(number) equals the expected result
    assert is_even(number) == expected
    pass
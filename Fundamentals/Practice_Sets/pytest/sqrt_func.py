import math

def calculate_square_root(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(n)


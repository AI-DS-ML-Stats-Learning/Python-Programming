numbers = [1, 2, 3, 4, 5]

def square_if_even(num):
    # Imagine this is a slow calculation!
    return num ** 2 if num % 2 == 0 else None


# Your Task: Write a single list comprehension that:

# Calls square_if_even(n) for each number.
# Filters out the None values.
# Crucial: You must use the Walrus Operator (:=) so that square_if_even is only called once per number.
# Example Output: [4, 16]

var = [y for i in numbers if (y:=square_if_even(i)) is not None]

print(var)
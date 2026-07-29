data = [
    [1, 2, 3], 
    [4, -5, 6], 
    [7, 8, 9]
]

# Filters data to keep only the sub-lists where all numbers are positive (greater than 0).
# Example Output: [[1, 2, 3], [7, 8, 9]] (Note: [4, -5, 6] is discarded because -5 is negative).

# Hint: Use all() inside the if clause at the end of the comprehension! Give it a try!

var = [j for j in data if all(k>0 for k in j)]

print(var)
matrix = [
    [1, 5, 8], 
    [12, 3, 14], 
    [7, 8, 9]
]

# Flattens this 2D matrix into a normal 1D list.
# Filters the list to only include numbers that are even.
# Example Output: [8, 12, 14, 8]

# Give it a try and remember the ordering rule for nested loops!

list1 = [j for i in matrix for j in i if j%2==0]
print(list1)
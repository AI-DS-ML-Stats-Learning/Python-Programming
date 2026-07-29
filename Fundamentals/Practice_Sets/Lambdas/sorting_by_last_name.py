names = ['Salil Gupta', 'Amit Sharma', 'Rahul Sen', 'Priya Roy']

# Your Task: 
# Write a code using sorted() and a lambda function as the key parameter to sort this list alphabetically by their last names.

# Example Output: ['Salil Gupta', 'Priya Roy', 'Rahul Sen', 'Amit Sharma']
# (Since G < R < Sen's S < Sharma's Sh)

# Write the code and explain how the lambda function splits the name to find the last name!

var = sorted(names, key = lambda name: name.split(' ')[1])

print(var)
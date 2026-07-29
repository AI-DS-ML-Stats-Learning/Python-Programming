students = [
    ('Salil', 'B'),
    ('Amit', 'A'),
    ('Rahul', 'C')
]

# Your Task: Write a code using sorted() and lambda to sort the students by their 
# grades in alphabetical order (A first, then B, then C).

# Hint: The lambda will receive ONE tuple at a time (e.g., ('Salil', 'B')). 
# How do you access the grade (the second element) of a tuple? Give it a try!

var = sorted(students, key = lambda grade : grade[1])

print(var)
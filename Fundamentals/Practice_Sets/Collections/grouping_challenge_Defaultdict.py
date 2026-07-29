# Scenario: You have a list of tuples representing city names and their countries:

locations = [
    ("India", "Mumbai"),
    ("USA", "New York"),
    ("India", "Delhi"),
    ("USA", "Chicago"),
    ("UK", "London")
]

# We want to group these cities by country so we get a dictionary that looks like 
# this: {'India': ['Mumbai', 'Delhi'], 'USA': ['New York', 'Chicago'], 'UK': ['London']}

# Your Task: Write Python code using defaultdict(list) to group the cities under their respective country keys 
# and print the resulting dictionary.

# Give it a shot! Think about how you loop over the tuples and append the city to the country key.

from collections import defaultdict

groups = defaultdict(list)

for name, group in locations:
    groups[name].append(group)

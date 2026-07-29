# Let's test this counting concept and compare it with the built-in Counter.

# Scenario: You have a list of words:

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# Your Task:

# Write the code using defaultdict(int) to count the occurrences of each word in the list.
# Write the code using Counter to do the exact same counting. (Notice how much shorter the Counter version is!).

from collections import defaultdict, Counter

groups = defaultdict(int)

for name in words:
    groups[name]+=1
print(groups)

 
groups = Counter(words)

print(groups)
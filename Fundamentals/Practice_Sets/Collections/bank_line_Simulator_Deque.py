# Let's move to deque (Double-ended Queue).

# Scenario: You are simulating a line of customers waiting at a bank. 
# The customers at the front of the line are served first, and new customers join at the back of the line 
# (this is a First-In, First-Out queue).

# Your Task:

# Import deque from collections.
# Create a queue named bank_queue containing: ['Salil', 'Amit', 'Rahul'].
# Add a new customer "Priya" to the back of the queue.
# Serve (remove and print) the customer at the front of the queue.
# Print the remaining queue.
# Conceptual Question: Why is using bank_queue.popleft() on a deque much faster than using list.pop(0) 
# on a normal Python list when the queue grows to millions of items?
# Give this a try! Think about the memory differences between lists and deques.

from collections import deque

bank_queue = deque(['Salil', 'Amit', 'Rahul'])

bank_queue.append("Priya")
bank_queue.popleft()

print(bank_queue)


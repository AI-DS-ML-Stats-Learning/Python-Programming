keys = ['port', 'host', 'username', 'password']
values = [8080, 'localhost', 'admin', None]

# Your Task: Write a single dictionary comprehension that:

# Combines these two lists into a dictionary where keys map to values.
# Filters out (excludes) any key-value pairs where the value is None.
# Example Output: {'port': 8080, 'host': 'localhost', 'username': 'admin'}

'''Both the solutions work well and with same time complexity O(n). Just that with zip, we are avoiding indexing here'''
# var = {keys[id]: value for id, value in enumerate(values) if value is not None}
var = {key: value for key, value in zip(keys, values) if value is not None}

# for var in values:
print(var)
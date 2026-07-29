products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Monitor', 'price': 300},
    {'name': 'Keyboard', 'price': 75}
]

# Your Task: Write a code using sorted() and a lambda function to sort these products by their price
# in ascending order (cheapest to most expensive).

# Hint: The lambda will receive one dictionary at a time (e.g., {'name': 'Laptop', 'price': 1200}). 
# How do you extract the price from that dictionary? Give it a shot!

var = sorted(products, key = lambda p:p['price'] )

# var = lambda product: product.get()

# list1 = [var(product) for product in products]

print(var)
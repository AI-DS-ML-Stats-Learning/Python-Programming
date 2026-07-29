result = (lambda x: (lambda y: x + y))(5)(10)

# What is the value of result?
# Explain step-by-step how Python evaluates this line. Why are there two sets of parentheses at the end: (5) and (10)?
print(result)

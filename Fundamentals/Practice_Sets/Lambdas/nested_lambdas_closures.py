# Question 13.7: Nested Lambdas & Closures
# Concept: A lambda can return another lambda. 
# The inner lambda will "remember" the variables of the outer lambda even after the outer lambda has finished running.
# This memory is called a Closure.

# Your Task:

# Write a function factory named make_power_function using a nested lambda. It should take an exponent n and return a function that raises its input to the power of n.
# Use your factory to create a square function (power of 2) and a cube function (power of 3).
# Test it by printing square(5) (should be 25) and cube(5) (should be 125).
# Conceptual Question: How does the inner lambda still know what n is when we call square(5), since the make_power_function call already completed?

make_power_function = lambda n: lambda x: x**n

'''this we are doing by creating defs and not closures'''
# def square(n):
#     print(make_power_function(2)(n))
# def cube(n):
#     print(make_power_function(3)(n))

'''here we are using the concept of closures'''
square = make_power_function(2)
cube = make_power_function(3)

print(square(5))
print(cube(5))
# Let's write a class with __slots__ and see how it enforces memory safety.

# Your Task:

# Define a class named Coordinates.
# Add __slots__ = ("x", "y") to the class.
# Define the constructor __init__(self, x, y) to initialize self.x and self.y.
# Create an instance: point = Coordinates(10, 20).
# Try to access point.__dict__. (What happens?)
# Try to add a new attribute: point.z = 30. (What happens?)
# Conceptual Question: Why does point.z = 30 fail?
# Give this a try to see how slots change the behavior of objects!

class Coordinates:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Coordinates(10,20)

# print(point.__dict__)
point.z = 30
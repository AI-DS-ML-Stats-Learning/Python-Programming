# Let's test if you can write a simple decorator now that you've seen the structure.

# Scenario: You want to write a decorator named @double_result. It should run the original function, 
# get the numeric result, multiply it by 2, and return the doubled value.

# Your Task: Complete this decorator implementation:

from functools import wraps

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Call the original function and save the result
        # print(f"Calling the original {func.__name__}")
        result = func(*args, **kwargs)
        # 2. Multiply that result by 2
        result = result*2
        # 3. Return the doubled result
        return result
        pass
    return wrapper

# Test it:
@double_result
def add(a, b):
    return a + b

print(add(5, 3))  # Should print 16 (since (5 + 3) * 2 = 16)
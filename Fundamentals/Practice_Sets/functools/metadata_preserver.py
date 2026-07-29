# Let's move to custom decorators and why we need functools.wraps.

# When you decorate a function, you are wrapping it inside another function.
# If you don't use @wraps, the original function loses its name and docstring (they get replaced by the wrapper's name).

# Your Task: Write a custom decorator named @log_execution that:

# Prints "Calling [function name]" before running the function.
# Runs the function and saves the result.
# Prints "Finished [function name]" after running.
# Returns the result.
# Uses @wraps(func) from functools to ensure the decorated function preserves its original identity.

from functools import wraps

def log_execution(func):
    # 1. @wraps copies the original function's name and docstring to the wrapper
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 2. Do something BEFORE the function runs
        print(f"Calling {func.__name__}")
        
        # 3. Call the original function using *args and **kwargs (to pass all arguments)
        result = func(*args, **kwargs)
        
        # 4. Do something AFTER the function runs
        print(f"Finished {func.__name__}")
        
        # 5. Return the final result
        return result
        
    # Return the inner wrapper function
    return wrapper

# Test it:
@log_execution
def greet(name):
    """Greets a user by name."""
    return f"Hello, {name}"

print(greet("Salil"))
print(greet.__name__)  # Should print "greet", not "wrapper"
print(greet.__doc__)   # Should print "Greets a user by name."
# Inside wrapper:
# Record the start time using start = time.time().
# Call the original function func(*args, **kwargs) and save the result.
# Record the end time using end = time.time().
# Print: "Function [name] took [time elapsed] seconds to run." (Use func.__name__ to get the name).
# Return the result.

import time
from functools import wraps

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Record start time
        start = time.time()
        # 2. Call func and save result
        result = func(*args, **kwargs)
        # 3. Record end time
        end = time.time()
        # 4. Print elapsed time
        print(f"Function {func.__name__} tool {end - start} seconds to run.")
        # 5. Return result
        return result
        pass
    return wrapper

# Test it:
@time_execution
def slow_calculation(n):
    """Simulates a heavy math calculation."""
    time.sleep(1)  # Sleep for 1 second to simulate slowness
    return n * 10

print("Result:", slow_calculation(5))
print("Name:", slow_calculation.__name__)  # Verify it is "slow_calculation"
from functools import partial

def log_message(level, user, message):
    return f"[{level.upper()}] User {user}: {message}"

# Your Task:

# Use partial to create a new function named log_salil where the user parameter is frozen as "Salil".

# When you call log_salil(level="info", message="Logged in"), it should output: [INFO] User Salil: Logged in
# Use partial to create a new function named log_system_error where both level is frozen as "ERROR" 
# and user is frozen as "SYSTEM".

# When you call log_system_error(message="Database down"), it should output: [ERROR] User SYSTEM: Database down
# Test both functions and print their outputs.

log_salil = partial(log_message, user = "Salil")
log_system_error = partial(log_message, level = "ERROR", user = "SYSTEM")

print(log_salil(level="info", message="Logged in"))
print(log_system_error(message="Database down"))
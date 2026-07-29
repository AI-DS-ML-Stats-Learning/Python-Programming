def log_generator():
    logs = [
        "INFO: Server started",
        "ERROR: DB Connection Lost",
        "INFO: User login successful",
        "WARNING: Disk space 90% full",
        "ERROR: API Timeout",
        "INFO: Report generated"
    ]
    # for log in logs:
    #     yield log
    yield from logs #this is the other way

# Call log_generator() to get the generator object.
# Write a Generator Expression (using parentheses (), 
# not square brackets []) that takes that log stream and filters out only the logs that contain the word "ERROR".
# 
# Write a small loop to print the filtered results.
# 
# Conceptual Question: Why is a Generator Expression much better than a List Comprehension 
# if this was a real-world server stream producing millions of logs per hour?
# 
# Give this a write-up and explain your answer!

obj = log_generator()

obj_gen = (i for i in obj if "ERROR" in i)

for i in obj_gen:
    print(i)


# Scenario: You have a binary log file named log.bin. 
# The developers put a 4-byte validation code (a checksum) at the very end of the file.

# Your Task: Write Python code that:

# Opens log.bin in binary read mode.
# Moves the file cursor to exactly 4 bytes before the end of the file using seek().
# Reads those final 4 bytes using read().
# Prints the resulting bytes.
# Let's see your code!

with open("log.bin", "rb") as file:
    file.seek(-4, 2)
    print(file.read(4))
# Let's write a custom context manager that mimics Python's open() function but prints messages to show us when 
# it is opening and closing the file.

# Your Task: Write a class named MyFileOpener that:

# Takes a filename and mode in its constructor __init__.
# 
# Implements __enter__ to open the file and print: "Opening file: [filename]", 
# and then returns the opened file object.
# 
# Implements __exit__ to close the file, print: "Closing file: [filename]", 
# and return False (so any exceptions are not suppressed).

class MyFileOpener:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.file_name}")
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
        print(f"Closing file: {self.file_name}")
        return False

with MyFileOpener("log.bin", "rb") as file:
    print("Reading data...")
    file.seek(-4, 2)
    print(file.read())
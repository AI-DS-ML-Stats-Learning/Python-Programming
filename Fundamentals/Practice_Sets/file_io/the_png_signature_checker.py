# Every PNG image file in the world starts with the exact same 8 bytes (known as its "magic numbers" or 
# file signature): b'\x89PNG\r\n\x1a\n'. We can use Python to verify if a file is actually a PNG image.

# Your Task: Write Python code that:

# Opens a file named picture.png in the correct binary read mode.
# Reads only the first 8 bytes of the file.
# Prints "Valid PNG" if the bytes match b'\x89PNG\r\n\x1a\n', otherwise prints "Corrupted or Invalid PNG".
# Uses with correctly and does not include any redundant .close() calls.
# Give it a shot! Think about how you open in binary mode and how to read a specific number of bytes.

name = []
with open("sample_for_png_checker.png", "rb") as file:
    name = file.read(8)

    if name == b'\x89PNG\r\n\x1a\n':
        print("Valid PNG")
    else:
        print("Corrupted or INvalid PNG")

print(name)
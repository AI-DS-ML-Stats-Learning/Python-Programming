# Your Task (Question 14): Write Python code that:

# Opens config.txt for reading.
# Opens a new file named cleaned.txt for writing.
# Reads config.txt line-by-line, and writes to cleaned.txt only the lines that do NOT start with #.

# with open("config.txt", "r") as file:
#     with open("cleaned.txt", "w") as cln_File:
#         for i in file:
#             if not i.startswith("#"):
#                 cln_File.write(i)
#     cln_File.close()
# file.close()

'''Better version'''

with open("config.txt", "r") as file, open("cleaned.txt", "w") as cln_File:
    for i in file:
        if not i.strip().startswith("#"):
            cln_File.write(i)



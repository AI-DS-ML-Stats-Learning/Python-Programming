# name = input("What is your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name  = f"{first} {last}"
# print(f"hello, {name}")

import re 

name = input("What is your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name) #elements in the parentheses are considered as groups, which can later be used 

if matches:
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
# names = []

# for i in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")

# file = open("names.txt","w") #write
# file = open("names.txt","a") 
# file.write(f"{name}\n")
# file.close()

# with  open("names.txt","a") as file:
# with  open("names.txt","r") as file:
#     # file.write(f"{name}\n")
#     lines = file.readlines()

# for line in lines:
#     print("hello, ", line.rstrip())

# with  open("names.txt","r") as file:
#     for line in sorted(file):
#         print("hello, ", line.rstrip())
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
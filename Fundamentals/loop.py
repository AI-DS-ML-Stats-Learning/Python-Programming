i = 0

# while i!=0:
#     print("meow")
#     i = i-1

# while i<3:
#     print("meow")
#     i = i+1

# for i in [0,1,2]:
#     print("meow")/

# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What is n? "))
#     # if n<0:
#     #     continue
#     # else:
#     #     break
#     if n>0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n>0:
            break
    return n

def  meow(n):
    for _ in range(n):
        print("meow")

main()
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break


    # while True:
    #     try:
    #         x = int(input("What's x? "))
    #         break
    #     except ValueError:
    #         print("x is not an integer")

# print(f"x is {x}")

def main():
    x = get_int("What is x ? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        # try:
        #     x = int(input("What's x? "))
        # except ValueError:
        #     print("x is not an integer")
        # else:
        #     # break
        #     return x
        try:
            return(int(input(prompt)))
        except ValueError:
            # print("x is not an integer")
            pass

main()
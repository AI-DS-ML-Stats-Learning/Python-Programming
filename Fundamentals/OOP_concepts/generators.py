def main():
    n = int(input("What is n? "))
    for i in sheep(n):
        print(i)

"""conventional method that will run into memory error if the input value is very high like 1M"""
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("sheep " * i)
#     return flock

"""using generator with "yield" keyword that generates one row at a time and hence we do not run into the memory issue"""
def sheep(n):
    for i in range(n):
        yield "sheep " * i

if __name__ == "__main__":
    main()
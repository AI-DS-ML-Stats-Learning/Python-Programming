import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# if len(sys.argv) < 2:
#     # print("Too few arguments")
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     # print("Too amny arguments")
#     sys.exit("Too amny arguments")
# else:
#     print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    # print("Too few arguments")
    sys.exit("Too few arguments")

# for arg in sys.argv[1::2]:
for arg in sys.argv[1:-1]: #-1 as end index means last element of the list as last elements can also be represented as negative index
    print("hello, my name is", arg)
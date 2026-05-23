# def main():
#     yell(["This", "is", "CS50"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

"""using *args"""
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()



"""using *args and map"""
def main():
    yell1("This", "is", "CS50")

def yell1(*words):
    uppercased1 = map(str.upper, words)
    print(*uppercased1)

if __name__ == "__main__":
    main()


"""using list comprehension"""

def main():
    yell2("This", "is", "CS50")

def yell2(*words):
    uppercased2 = [word.upper() for word in words]
    print(*uppercased2)

if __name__ == "__main__":
    main()
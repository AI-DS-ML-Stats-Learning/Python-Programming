

def meow(n: int) -> None:
    """
    This is a docstring comment section

    :param n: number of times to meow
    :type n: int
    :raise TypeError: IF n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))

meow(number)
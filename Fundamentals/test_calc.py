# from calc import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared is not 4")
#     try:
#         assert square(3) == 9
#     except:
#         print("3 squared is not 9")
#     try:
#         assert square(-2) == 4
#     except:
#         print("-2 squared is not 4")




# if __name__ == "__main__":
#     main()

from Fundamentals.calc import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_str1():
    with pytest.raises(NameError):
        square("cat")
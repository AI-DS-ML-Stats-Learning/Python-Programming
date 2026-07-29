# Your Task: Write a Pytest script (named test_cart.py) that:

# Imports pytest and ShoppingCart (assume it is in a file named cart.py).
# Defines a @pytest.fixture named empty_cart that creates and returns (yields) a new ShoppingCart() instance.
# Writes two tests:
# test_empty_cart_length(empty_cart): Asserts that a new cart starts with total_items() == 0.
# test_add_one_item(empty_cart): Adds "Apple" to the cart and asserts that total_items() == 1.
# Hint: Pass the name of your fixture (empty_cart) as a parameter to your test functions. 
# Pytest will automatically call the fixture and pass the returned cart object into the tests! Let's see your code.

import pytest
from ShoppingCart import ShoppingCart

@pytest.fixture
def empty_cart():
    new_Shop = ShoppingCart()
    yield new_Shop

def test_empty_cart_length(empty_cart):
    assert empty_cart.total_items() == 0

def test_add_one_item(empty_cart):
    empty_cart.add_item("Apple")
    assert empty_cart.total_items() == 1



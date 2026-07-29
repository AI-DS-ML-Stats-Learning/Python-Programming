# Let's write a simple Abstract Base Class to see how Python enforces rules.

# Scenario: You are building a payment processing system. All payment methods (like Credit Card, PayPal)
# must have a process_payment(amount) method.

# Your Task:

# Import ABC and abstractmethod from the abc module.
# Define an abstract class named PaymentMethod.
# Add an abstract method named process_payment(self, amount) inside it.
# Create a subclass named CreditCard that inherits from PaymentMethod.
# Intentionally leave it empty (just write pass inside CreditCard).
# Try to create a CreditCard object: cc = CreditCard().
# Conceptual Question: What error does Python throw when you run this? Why?
# Give this a shot to see Python's runtime interface enforcement in action!

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount=200):
        self.amount = amount

'''
Fix your CreditCard class by implementing the process_payment(self, amount) method so it prints: 
                                                    "Processing credit card payment of $[amount]".
Write a function named checkout(payment_obj, amount) that calls the process_payment(amount) method of the passed payment object.
Test your code by instantiating CreditCard and passing it to the checkout function.'''

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

def checkout(payment_obj, amount):
    payment_obj.process_payment(amount)

cc = CreditCard()

checkout(cc, 100)
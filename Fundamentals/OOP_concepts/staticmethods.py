class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    @staticmethod
    def print_details(temp):
        print("This method can print static values. " \
        "It can also take parameters which can be passed at the time of object creation or when trying to access this method")
        print(f"Temperature entered is {temp}")

Student.print_details(78)
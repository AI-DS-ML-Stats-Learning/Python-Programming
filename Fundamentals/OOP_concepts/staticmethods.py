class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    @staticmethod
    def print_details():
        print(self.m1, self.m2)

s1 = Student(12, 30)
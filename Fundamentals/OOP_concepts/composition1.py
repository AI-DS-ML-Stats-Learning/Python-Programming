class House:
    def __init__(self, location):
        self.location = location
    
    def print_details(self):
        print(f"Student has house at {self.location}")
    
class Flat:
    def __init__(self, location):
        self.location = location

    def print_details(self):
        print(f"Student has flat at {self.location}")

class Student:
    def __init__(self,student, house_obj, flat_obj):
        self.house_obj = house_obj
        self.flat_obj = flat_obj
        self.student = student

    def print_details(self):
        print(f"This is {self.student}")
        self.flat_obj.print_details()
        self.house_obj.print_details()
    
# house_obj = House("BUrrabazar")
# flat_obj = Flat("Behala")
s1 = Student("Salil", House("BUrrabazar"), Flat("Behala"))
s1.print_details()
# s1.house_obj.print_details()
# s1.flat_obj.print_details()
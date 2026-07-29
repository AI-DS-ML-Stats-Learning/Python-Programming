class House:
    def __init__(self, location):
        self.location = location
        print(f"Student has house at {self.location}")
    
class Flat:
    def __init__(self, location):
        self.location = location
        print(f"Student has flat at {self.location}")

class Student:
    def __init__(self,student, house_obj, flat_obj):
        self.house_obj = house_obj
        self.flat_obj = flat_obj
        self.student = student
        print(f"This is {self.student}")
    
# house_obj = House("BUrrabazar")
# flat_obj = Flat("Behala")
s1 = Student("Salil", House("BUrrabazar"), Flat("Behala"))
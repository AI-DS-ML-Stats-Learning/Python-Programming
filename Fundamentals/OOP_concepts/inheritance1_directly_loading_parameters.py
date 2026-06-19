'''Accessing the super class variables using variables names to the constructor'''
class School:
    school_name = "RN Singh Memorial High School"

    def __init__(self, location, pincode, capacity):
        self.location = location
        self.pincode = pincode
        self.capacity = capacity
    
    def print_details(self):
        print(f"{self.__class__.school_name} is located in {self.location} at pincode {self.pincode}")

class Student(School):
    def __init__(self, name, age, gender, class_n, location, pincode, capacity):
        super().__init__(location, pincode, capacity)
        self.name = name
        self.age = age
        self.gender = gender
        self.class_n = class_n

# s1 = School("Sirmani Market", 700006, 400)

s1  = Student("Salil", 18, "M", "History", "Sirmani Market", 700006, 400)

print(s1.school_name)
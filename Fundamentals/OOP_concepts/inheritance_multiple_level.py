class House:
    def __init__(self, house_name, house_age, **kwargs):
        super().__init__(**kwargs)
        self.house_name = house_name
        self.house_age = house_age
    
    def print_details(self):
        print(f"{self.house_name} is of age {self.house_age}")
        

class School:
    school_name = "RN Singh Memorial High School"
    def __init__(self, location, pincode, capacity, **kwargs):
        super().__init__(**kwargs)
        self.location = location
        self.pincode = pincode
        self.capacity = capacity
    
    def print_details(self):
        print(f"{self.__class__.school_name} is located in {self.location} at pincode {self.pincode}")
        # super().print_details()

class Student(School, House):
    def __init__(self, name, age, gender, class_n, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
        self.gender = gender
        self.class_n = class_n

    def print_details(self):
        # return super().print_details()
        School.print_details(self)
        House.print_details(self)

# s1 = School("Sirmani Market", 700006, 400)

s1  = Student("Salil", 18, "M", "History", location = "Sirmani Market", pincode = 700006, capacity = 400
              , house_name = "DTC Downtown", house_age = 4)

s1.print_details()
# print(s1.school_name)
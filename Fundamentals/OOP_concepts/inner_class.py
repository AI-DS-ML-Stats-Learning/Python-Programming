class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    
    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.cap = 8


s1 = Student("Salil", 28)
# l1 = Student.Laptop()

print(s1.name, s1.age)
# print(l1.model, l1.cap)
# print(s1.Laptop().model, s1.Laptop().cap)
print(s1.lap.model, s1.lap.cap)
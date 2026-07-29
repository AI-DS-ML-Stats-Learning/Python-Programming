class Student:
    def execute(self):
        print("Invoking Parent CLass")

class Teacher(Student):
    def execute(self):
        print("Invoking Child Class. Overriding Parent Class")

t1 = Teacher()

t1.execute()
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    def print_(self):
        print(self.name, "in ", self.house)

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject 

    def print_(self):
        print(self.name, "teaches ", self.subject)

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

student.print_()
professor.print_()
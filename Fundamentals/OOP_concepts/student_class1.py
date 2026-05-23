class Student:
    # ...
    def __init__(self, name, house):
        # if not name:
        #     raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Racvenclaw", "Slytherin"]:
        #     raise ValueError("Ivalid House")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} in {self.house}"
    
    #decorators
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    #Getter -> gets value
    @property
    def house(self):
        return self._house
    
    #setter -> set value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Racvenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    student._house = "Accessing Class variables"
    print(student)

def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) #constructor call

if __name__ == "__main__":
    main()
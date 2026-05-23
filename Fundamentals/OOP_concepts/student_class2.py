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
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
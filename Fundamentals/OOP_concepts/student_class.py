class Student:
    # ...
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Racvenclaw", "Slytherin"]:
            raise ValueError("Ivalid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} in {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case "Jack Russell":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) #constructor call

if __name__ == "__main__":
    main()
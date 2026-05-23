def main():
    # name  = get_name()
    # house = get_house()
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student()
    # list vs tuples
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")

    # using dict
    # print(f"{student["name"]} from {student["house"]}")
    if student["name"] == "Padma":
        student["house"] = "ravenclaw"
    print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

def get_student():
    # name = input("Name: ")
    # house = input("House: ")
    # return name, house
    # return [name, house]
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
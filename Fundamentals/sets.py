students = [
    {"name": "Hermione", "house": "Ravenclaw"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor" },
    {"name": "Draco", "house": "Slytherin"},
]


## using list to get unique values
# houses = []

# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)



## using set to get unique values

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
students = [
    {"name": "Hermione", "house": "Ravenclaw"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

"""using list compprehension"""
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


"""using filter"""


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)
gryffindors = filter(lambda s : s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

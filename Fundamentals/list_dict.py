# using list
# students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])

# using dict

# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students = {"Hermione":"Gryffindor", 
#             "Harry":"Gryffindor", 
#             "Ron":"Gryffindor",
#             "Draco":"Slytherin"
#             }

# # print(students["Hermione"])
# # print(students["Harry"])
# # print(students["Ron"])
# # print(students["Draco"])

# for student in students:
#     print(student, students[student], sep = " - ")

# using dict to associate multiple things

# students = {"Hermione":["Gryffindor", "Patronus"], 
#             "Harry":"Gryffindor", 
#             "Ron":"Gryffindor",
#             "Draco":"Slytherin"
#             }

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus":None},
]

for s in students:
    print(s["name"], s["house"], s["patronus"], sep=" - ")
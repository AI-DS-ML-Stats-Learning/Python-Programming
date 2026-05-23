students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for s in students:
#     gryffindors.append({"name": s, "house":"Gryffindor"})

"""using dict comprehension"""
# gryffindors = [{"name": s, "house": "Gryffindor"} for s in students] """list comprehension"""

gryffindors = {s: "Gryffindor" for s in students}

print(gryffindors)


print(" ")
"""adding ranks"""

for i in range(len(students)):
    print(i + 1, students[i])

print(" ")
"""using enumerate"""
for i, student in enumerate(students):
    print(i + 1, student)

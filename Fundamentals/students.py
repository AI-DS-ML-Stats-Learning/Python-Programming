# import csv

# students = []

# with open("students.csv") as file:
#     # for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         # name, house = line.rstrip().split(",")
#         # students.append(f"{name} is in {house}")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         # student = {"name":name, "house":house}
#         # students.append(student)
#     reader =csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "house":row[1]})

#     for name, house in reader:
#         students.append({"name": name, "house":house})

# # def get_name(student):
# #     return student["name"]

# for student in sorted(students, 
#                     #   key = get_name, 
#                     key = lambda student: student["name"],
#                     reverse=True):
#     print(f"{student['name']} is in {student['house']}")


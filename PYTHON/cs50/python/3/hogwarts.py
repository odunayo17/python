students = [
        {"name":"Hermionie","house":"Gryffindor","patroneuos":"Otter"},
        {"name":"Harry","house":"Gryffindor","patroneuos":"Stag"},
        {"name":"Ron","house":"Gryffindor","patroneuos":"Jack Russell Terrier"},
        {"name":"Draco","house":"Slytherin","patroneuos":None}
        ]  
for student in students:
    print(student["name"], student["house"], student["patroneuos"], sep=", ")

"""
students = {
        "Hermionie":"Gryffindor",
        "Harry":"Gryffindor",
        "Ron":"Gryffindor",
        "Draco":"Slytherin",
}
for student in students:
    print(student, students[student], sep=": ")

"""




"""students = {
        "Hermionie":"Gryffindor",
        "Harry":"Gryffindor",
        "Ron":"Gryffindor",
        "Draco":"Slytherin",
}

print(students ["Hermionie"])
print(students ["Harry"])
print(students ["Ron"])
print(students ["Draco"])

"""

"""students = ["Hermionie","Harry","Ron"]

for i in range (len(students)):
    print(i + 1,students [i])
"""


"""
students = ["Hermionie","Harry","Ron"]

for s in students:
    print(s)


students = ["Hermionie","Harry","Ron"]

print(students [0])
print(students [1])
print(students [2])
"""
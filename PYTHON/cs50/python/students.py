with open("students.csv") as file:
    for line in file:
        name,school = line.rstrip().split(",")
        print(f"{name} is in {school}")











"""with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")"""
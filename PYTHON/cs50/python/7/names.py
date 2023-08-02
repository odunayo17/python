names = []
with open("names.txt" , "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello,{name}!")















"""with open("names.txt" , "r") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())"""



"""with open("names.txt" , "r") as file:
    for line in file:
        print("hello,",line.rstrip())"""




















"""with open("names.txt" , "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,",line.rstrip())"""






"""name = input("what's your name? ")

with open("names.txt" , "a") as file:

    file.write(f"{name}\n")"""











"""name = input("what's your name? ")

file = open("name.txt" , "a")

file.write(f"{name}\n")
file.close()"""














"""name = input("what's your name? ")

file = open("name.txt" , "w")

file.write(name)
file.close()"""







"""names = []
for _ in range(3):
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"Hello,{name}!")"""
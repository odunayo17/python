import math

print("Scientific Calculator")
print("Enter 'quit' to exit")

while True:
    # take input from user
    user_input = input("Enter an equation: ")

    # exit program if user enters 'quit'
    if user_input == 'quit':
        break

    # evaluate the expression
    try:
        result = eval(user_input)
    except:
        print("Invalid input")
        continue

    # print the result
    print("Result:", result)
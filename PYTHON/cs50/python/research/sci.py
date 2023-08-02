import math

def scientific_calculator():
    print("Scientific Calculator")
    print("---------------------")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("0. Exit")

    while True:
        choice = int(input("Enter operation number (0-10): "))

        if choice == 0:
            print("Exiting the calculator...")
            break
        elif choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = num1 + num2
                print("Result: ", result)
            elif choice == 2:
                result = num1 - num2
                print("Result: ", result)
            elif choice == 3:
                result = num1 * num2
                print("Result: ", result)
            elif choice == 4:
                result = num1 / num2
                print("Result: ", result)
            elif choice == 5:
                result = num1 ** num2
                print("Result: ", result)
                
        elif choice in [6, 7, 8, 9, 10]:
            num = float(input("Enter the number: "))

            if choice == 6:
                result = math.sqrt(num)
                print("Result: ", result)
            elif choice == 7:
                result = math.sin(num)
                print("Result: ", result)
            elif choice == 8:
                result = math.cos(num)
                print("Result: ", result)
            elif choice == 9:
                result = math.tan(num)
                print("Result: ", result)
            elif choice == 10:
                result = math.log10(num)
                print("Result: ", result)
        else:
            print("Invalid choice. Please try again.")

        print()  # Print an empty line for readability

scientific_calculator()

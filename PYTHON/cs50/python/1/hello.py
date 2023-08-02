def main():
    name = input("what's your name? ")
    hello(name)


def hello(to="world"):
    print("hello", to)


main()
"""
name = input("what's your name? ").strip().title()

print(f"hello, {first}")


 split user name to first and last name
first, last = name.split(" ")

 remove white space

 Capitalize name (name = name.capitalize())
 title method name = name.title()


print("hello,", end="",sep="")
"""

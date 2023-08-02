def main():
    name = input("what's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,",to)

if __name__ == "__main__":
    main()
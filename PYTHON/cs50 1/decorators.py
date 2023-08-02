def announce(f):
    def wrapper():
        print("about to run program...")
        f()
        print("done with program...")
    return wrapper


@announce
def hello():
    print("hello mother fucker")

hello()    
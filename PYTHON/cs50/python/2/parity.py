def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even Number")

    else:
            print("Odd Number")



def is_even(n):

    return n % 2 == 0 
   # return True if n % 2 == 0 else False
  
main()









"""
x = int(input("what's x?"))

if x % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")
    """
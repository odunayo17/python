from random import randint

number = int(input("Guess a number between 1-10: "))
randnum = randint(1,10)

if number == randnum:
    print("You got it right 😃!")

elif  number < 1:
    print("number is to low")

elif  number > 10:
    print("number is to high")

else:
    print("You are wrong 😕!")
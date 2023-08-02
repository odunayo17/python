from random import choice

options = ["rock", "paper", "scissors"]

def game():
    players_choice = input("choose Rock,Paper,Scissors: ")

    while players_choice not in options:
        players_choice = ("invalid input choose again: ")

    computers_choice = choice(options)

    if players_choice == computers_choice:
        print(f"it's a draw you choose {players_choice} and computer choose {computers_choice}")

    elif players_choice == "rock" and computers_choice == "scissors":
        print(f"you choose {players_choice} and computer choose {computers_choice} you won🎉😃!")

    elif players_choice == "paper" and computers_choice == "rock":
        print(f"you choose {players_choice} and  computer choose {computers_choice}you won🎉😃!")

    elif players_choice == "scissors" and computers_choice == "paper":
        print(f" you choose {players_choice} and computer choose {computers_choice} you won🎉😃!")

    else:
        print(f"you choose {players_choice} and computer choose {computers_choice} you loose😕!")

game()








"""



def game():
    player_choice = input("choose rock paper scissors: ").title

    while player_choice not in options:
        players_choice = input("Invalid choice. Choose rock, paper, or scissors: ")

    computers_choice = choice(options)

    if player_choice == computers_choice:
        print("its a draw")

    elif player_choice == "Rock" and computers_choice == "Scissors":
        print(f"computer choose {computers_choice} and you choose {player_choice} you won!")

    elif player_choice == "Paper" and computers_choice == "Rock":
        print(f"computer choose {computers_choice} and you choose {player_choice} you won!")

    elif player_choice == "Scissors" and computers_choice == "Paper":
        print(f"computer choose {computers_choice} and you choose {player_choice} you won!")

    else:
        print("you loose")

game()"""
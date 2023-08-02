def get_choices():
    player_choice = input("enter a choice (rock,paper, scissors)")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


    choices = get_choices()
    print(choices)

def check_win(player,computer):
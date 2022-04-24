import random

play_game = True
opponent_choice = ""
user_choice = ""
invalid_input = False


def computer_choice():
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.randrange(0, 3)
    return choices[comp_choice]


def validate_input(input):
    if input == "rock" or input == "paper" or input == "scissors":
        return True
    else:
        print("Please enter a valid choice.")
        return False


def compare_input(user, computer):
    if user == "rock" and computer == "scissors":
        print("YOU WIN")
    elif user == "rock" and computer == "paper":
        print("YOU LOSE")
    elif user == "scissors" and computer == "paper":
        print("YOU WIN")
    elif user == "scissors" and computer == "rock":
        print("YOU LOSE")
    elif user == "paper" and computer == "rock":
        print("YOU WIN")
    elif user == "paper" and computer == "scissors":
        print("YOU LOSE")
    elif user == computer:
        print("YOU TIED")


def play_again():
    invalid = False
    while not invalid:
        again = input("Would you like to play again?(y/n) ")
        if again.lower() == "y" or again.lower() == "yes":
            invalid = True
            return True
        elif again.lower() == "n" or again.lower() == "no":
            return False
        else:
            print("Please enter 'y' or 'n'.")


print("Let's play Rock, Paper, Scissors!")

while play_game:
    invalid_input = False
    while not invalid_input:
        user_choice = input("Make your choice: ")
        invalid_input = validate_input(user_choice.lower())
    opponent_choice = computer_choice()
    print("Opponent chose " + opponent_choice)
    compare_input(user_choice.lower(), opponent_choice)
    play_game = play_again()

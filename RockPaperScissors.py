
import random

def user_selected(user_info, options):
    while True:
        if user_info in options:
            break
        else:
            print("You didn't select a valid option. Please, try again.")
            user_info = input("Please, choose between Rock, Paper and Scissors: ")
            continue

def play_game(user_info, options):
    random_option = random.choice(options)
    if user_info == random_option:
        print(f"Wow! You chose {user_info}, and the computer chose {random_option}. Then, I think we have a draw here.")
    elif user_info == "rock" and random_option == "scissors" or user_info == "paper" and random_option == "rock" or user_info == "scissors" and random_option == "paper":
        print(f"Amazing! You chose {user_info}, and the computer chose {random_option}. For that reason, you are the winner.")
    else:
        print(f"Sorry, you chose {user_info}, and the computer chose {random_option}. You loose this time.")
    
def main():
    options = ["rock", "paper", "scissors"]
    user_info = input("Please, choose between Rock, Paper and Scissors: ")
    user_info = user_info.lower()
    user_selected(user_info, options)
    play_game(user_info, options)

if __name__ == '__main__':
    main()

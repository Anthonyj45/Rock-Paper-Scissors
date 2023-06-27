
import random

def piedras_Papel(user_selected):
    options = ["Rock", "Paper", "Scissors"]
    """
    In  a variable named as random_solution, it will be saved the function random.choice which return a random element from our list.
    """
    random_Solution = random.choice(options)
    """
    It's necessary to save in lowercase two new variables the strings that were taken from the user.
    If the user submit a string with a different case, then will not be any trouble.
    And the code becomes simpler because of the .lower() attribute is called once, and not multiple times.
    
    The .capitalize() attribute will modify the string, and it will always start with an Uppercase.
    """
    user_Sel = user_selected.lower().capitalize()
    ran_Sol = random_Solution.lower().capitalize()

    if user_Sel == ran_Sol:
        print(f"You chose {user_Sel}, and the computer chose {ran_Sol}, So it is a draw.")
    elif (user_Sel == "Rock" and ran_Sol == "Scissors") or (user_Sel == "Paper" and ran_Sol == "Rock") or (user_Sel == "Scissors" and ran_Sol == "Paper"):
        print(f"You chose {user_Sel}, and the computer chose {ran_Sol}, So you won.")
    elif (user_Sel == "Rock" and ran_Sol == "Paper") or (user_Sel == "Paper" and ran_Sol == "Scissors") or (user_Sel == "Scissors" and ran_Sol == "Rock"):
        print(f"You chose {user_Sel}, and the computer chose {ran_Sol}, So you lost.")
    else:
        print("You didn't select a correct option. Please, Try again..")

if __name__ == '__main__':
    while True:
        user_selected = input("Please, choose between Rock, Paper or Scissors: ")
        if user_selected == "Rock" or user_selected == "Paper" or user_selected =="Scissors":
            piedras_Papel(user_selected)
            break
        else:
            continue

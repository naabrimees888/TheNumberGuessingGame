"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
print("Welcome to number guessing game!")
random_number = random.randint(1, 10)
tries = 0

try:
    user_number = int(input("Guess a number between 1 and 10: "))
except ValueError:
    print("Oops, it is not a number... Please try again!")
else:

    while True:
        tries += 1
        if random_number > user_number:
            print("It's higher")
            try:
                user_number = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Oops, it is not a number... Please try again!")
                continue
        elif random_number < user_number:
            print("It's lower")
            try:
                user_number = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Oops, it is not a number... Please try again!")
            continue
        else:
            if random_number == user_number:
                print("You got it! The number was: {} and you had {} tries".format(random_number, tries))
                break
# Kick off the program by calling the start_game function.
start_game()

# new_game = input("Would you like to play a new game? Yes/No ")
# new_game.lower()
# if new_game == "yes":
#      start_game()
# else:
#     print("Thank you for playing this game!")
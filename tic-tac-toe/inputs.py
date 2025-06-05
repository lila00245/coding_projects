#----------------------------------------------------------------------------------------------------------------
# inputs.py
# this file contains the functions to prompt user input and computer input
# it checks for valid input and keeps track of spots already taken
#----------------------------------------------------------------------------------------------------------------

import random
from board import spots_taken
from board import all_spots

def prompt_user_input () -> str :
    '''
    prompts for user input, accepts any number 1-9 and 'q' or 'quit' 
    returns a string
    '''
    user_choice = input("enter spot on board [1-9]: ")
    if (user_choice == 'q' or user_choice == 'quit') :      # for quitting program 
        print("quitting program..") 
        return user_choice
    elif not user_choice.isdigit() :                        # if input is not a digit, asks again
        print(f"\t{user_choice} is not a number, try again")
        user_choice = prompt_user_input()
    elif (int(user_choice) < 1 or int(user_choice) > 9) :   # if number is not in range, asks again
        print(f"\t{user_choice} is not between 1 and 9, try again")
        user_choice = prompt_user_input()
    elif int(user_choice) in spots_taken :                  # if number is already taken, asks again
        print(f"\t{user_choice} has already been chosen, try again")
        user_choice = prompt_user_input()
    else : # otherwise, append to keep track of spaces already used
        spots_taken.append(int(user_choice))
    return user_choice  # returns value for main program

def prompt_comp_input () -> int :
    '''
    this is where the computer makes a random choice based off which spaces are left
    returns an integer value
    '''
    #TODO: add more complexity to computer choice, rn it is random
    computer_choice = random.choice(all_spots)
    if computer_choice in spots_taken : # if value is already chosen, chooses again
        computer_choice = prompt_comp_input()
    else :  # otherwise, appends value so is not chosen again
        spots_taken.append(computer_choice)
    return computer_choice

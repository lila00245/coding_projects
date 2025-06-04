#----------------------------------------------------------------------------------------------------------------
# main.py
#----------------------------------------------------------------------------------------------------------------

import random
import inputs
import board
from board import spots_taken

'''
some thoughts of adding more complexity --> 
            choosing who starts first (user or computer), rn it defaults to user
            and if you want to be 'x' or 'o', rn user = X and comp = O
            get the computer to 'strategically' place it's spots, rn it's randomized
            
'''

def main () :
    print("welcome to tic-tac-toe!\nyou will be 'X' and computer will be 'O'\ntype 'q' or 'quit' to end game, good luck!")
    tic_tac_toe = board.create_og_board()
    # keeps looping until end of game (when)
    while True:
        user_choice = inputs.prompt_user_input()
        # ends loop if user types 'q' or 'quit'
        if (user_choice == 'q' or user_choice == 'quit') :
            break
        else :
            computer_choice = inputs.prompt_comp_input()
            print(f"you chose: {user_choice}")
            board.add_spot(tic_tac_toe, int(user_choice), "X")
            board.print_board(tic_tac_toe)
            print(f"computer chose: {computer_choice}")
            board.add_spot(tic_tac_toe, computer_choice, "O")
            board.print_board(tic_tac_toe)

    print(spots_taken)

if __name__ == "__main__" :
    main()

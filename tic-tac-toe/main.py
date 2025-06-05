#----------------------------------------------------------------------------------------------------------------
# main.py
# this is the main file to run the tic-tac-toe game
#----------------------------------------------------------------------------------------------------------------

import inputs
import board

'''
some thoughts of adding more complexity --> 
            choosing who starts first (user or computer), rn it defaults to user
            and if you want to be 'x' or 'o', rn user = X and comp = O
            get the computer to 'strategically' place it's spots, rn it's randomized
            
'''

def main () :
    '''
    main function to run the tic-tac-toe game
    '''
    moves = 0
    print("\nwelcome to tic-tac-toe! \nyou will be 'X' and computer will be 'O' \ntype 'q' or 'quit' to end game, good luck! \n")

    tic_tac_toe = board.create_og_board()
    # keeps looping until end of game (when)
    while True:
        user_choice = inputs.prompt_user_input()
        moves += 1
        # ends loop if user types 'q' or 'quit'
        if (user_choice == 'q' or user_choice == 'quit') :
            break
        print(f"\nyou chose: {user_choice}")
        board.add_spot(tic_tac_toe, int(user_choice), "X")
        board.print_board(tic_tac_toe)
        if moves >= 9 :
            print("tie game!")
            break
        computer_choice = inputs.prompt_comp_input()
        moves += 1
        print(f"computer chose: {computer_choice}")
        board.add_spot(tic_tac_toe, computer_choice, "O")
        board.print_board(tic_tac_toe)
    print("\nfinal board results: ")
    board.print_board(tic_tac_toe)
    if moves >= 9 :     # TODO: add more complexity to check for winner, only ask to play again if there is a winner or a tie
        play_again = input("would you like to play again? (y/n): ").lower()
        print()
        if play_again == 'y' or play_again == 'yes':
            main()

if __name__ == "__main__" :
    main()

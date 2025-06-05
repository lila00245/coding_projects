#----------------------------------------------------------------------------------------------------------------
# board.py
# this file contains the functions to create the board, print the board, and add spots to the board
#----------------------------------------------------------------------------------------------------------------

all_spots = [   1, 2, 3,    # for computer to random choose one
                4, 5, 6, 
                7, 8, 9 ]
spots_taken = []            # append once user or comp chooses a spot so the same spot is not used more than once


def create_og_board () :
    '''
    creates the original board, returns a 2D list
    '''
    board = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_board(board)
    return board


def print_board (board) -> str :
    '''
    prints the board in a readable format
    '''
    board_str = ""
    for i in range(3) :
        for j in range(3) :
            board_str += "| " + str(board[i][j]) + " "
        board_str += "|\n"
    print(board_str)
    
    
def add_spot (board, choice: int, user: str) -> None :     
    '''
    board is the updated board, choice is an integer btwn 1 and 9 , user is X or O
    adds a spot to the board based on user input, updates the board
    '''
    if choice >= 1 and choice <= 3 :
        board[0][choice-1] = user
    elif choice >= 4 and choice <= 6 : 
        board[1][choice-4] = user
    elif choice >= 7 and choice <= 9 : 
        board[2][choice-7] = user

from board import Board, spot_exists

class User:
    current_player = ' ' 

    def __init__(self, symbol):
        self.symbol = symbol

def get_input(choice):
    return input(choice)

# may not be working as expected all inputs come in as string...even keyboard nums
def spot_choice():
    response = get_input("Choose number from 1-9: ")
    if spot_exists(board.board_state, response) == True:
        return response
    else: 
        return false



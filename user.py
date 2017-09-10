from board import Board, spot_exists

class User:
    current_player = 'X' 

    def __init__(self, symbol):
        self.symbol = symbol

def get_input(choice):
    return input(choice)

# may not be working as expected all inputs come in as string...even keyboard nums
def spot_choice():
    spot_list = []
    spot_list.extend(range(1, len(Board.board_state) + 1))
    spot_list = list(map(str, spot_list))
    response = get_input("Choose number from 1-9: ")
    if response in spot_list:
        response = int(response)
    else:
        print('invalid choice')
        spot_choice()

    if spot_exists(Board.board_state, response) and is_occupied(Board.board_state, response) == False):
        Board.update_state(Board.board_state, User.current_player, response)
    else:
        print("spot is occupied")
        spot_choice()
    return response
        

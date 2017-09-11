from board import Board, spot_exists, is_occupied

class User:
    current_player = 'X' 

    def __init__(self, symbol):
        self.symbol = symbol

def get_input(choice):
    return input(choice)

# may not be working as expected all inputs come in as string...even keyboard nums
def spot_choice(current_state):
    spot_list = []
    spot_list.extend(range(1, len(current_state) + 1))
    spot_list = list(map(str, spot_list))
    print(spot_list)
    response = get_input("Choose number from 1-9: ")
    if response in spot_list:
        response = int(response)
    else:
        return 'invalid choice'
    if spot_exists(current_state, response) and is_occupied(current_state, response) == False:
        print(current_state, User.current_player, response)
        Board.update_state(current_state, User.current_player, response)
    else:
        return 'spot is occupied'
    return response
       

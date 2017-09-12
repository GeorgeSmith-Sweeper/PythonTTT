from board import Board, spot_exists, is_occupied, update_state

class User:
    # later iterations will not be hardcoded
    current_player = 'X' 

    def __init__(self, symbol):
        self.symbol = symbol

def get_input(choice):
    return input(choice)

def spot_validation(current_state, response):
    spot_list = []
    spot_list.extend(range(1, len(current_state) + 1))
    spot_list = list(map(str, spot_list))

    if response not in spot_list:
        # add ui error message
        return False
    else:
        response = int(response)
        if is_occupied(current_state, response):
            # add ui "That spot has already been selected! Pick again."
            return False
        else:
            return response

def turn_swap(the_current_player, opponent):
    if the_current_player == User.current_player:
        User.current_player = opponent
        return User.current_player 
    else: 
        return the_current_player

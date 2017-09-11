from board import Board, spot_exists, is_occupied, update_state

class User:
    # later iterations will not be hardcoded
    current_player = 'X' 

    def __init__(self, symbol):
        self.symbol = symbol

def get_input(choice):
    return input(choice)

def spot_choice(current_state):
    spot_list = []
    spot_list.extend(range(1, len(current_state) + 1))
    spot_list = list(map(str, spot_list))
    response = get_input("Choose number from 1-9: ")
    if response not in spot_list:
        print('That spot doesn\'t exist! Pick again.')
        return 'invalid choice'
    else:
        response = int(response)
        if is_occupied(current_state, response) == True:
            print('That spot has already been selected! Pick again.')
            return 'spot is occupied' 
        else:
            update_state(current_state, User.current_player, response)
            return response
    '''
    if spot_exists(current_state, response) and is_occupied(current_state, response) == False:
        update_state(current_state, User.current_player, response)
    else:
        print('That spot has already been selected! Pick again.')
        return 'spot is occupied'
    return response
    '''
#create turn swap function
def turn_swap(the_current_player, opponent):
    if the_current_player == User.current_player:
        User.current_player = opponent
        return opponent
    else: 
        return the_current_player

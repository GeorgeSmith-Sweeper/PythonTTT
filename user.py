from board import Board, SpotStates 
from ui import Ui

class User:
    current_player = 'X' 

    # players will be able to pick a symbol
    def __init__(self, symbol):
        self.symbol = symbol

    def switch_current_user(who_moved, opponent):
        if who_moved == User.current_player:
            User.current_player = opponent
            return User.current_player 
        else: who_moved 

def get_input(choice):
    return input(choice)

class UserActions:   
    def make_move(current_state, response):
        spot_list = []
        spot_list.extend(range(1, len(current_state) + 1))
        spot_list = list(map(str, spot_list))

        if response not in spot_list:
            Ui.msg("That spot doesn't exist. Try again.")
            return False
        else:
            response = int(response)
            if SpotStates.is_occupied(current_state, response):
                Ui.msg("That spot has already been selected! Try again.")
                return False
            else:
                return response

def switch_current_user(who_moved, opponent):
    if who_moved == User.current_player:
        User.current_player = opponent
        return User.current_player 
    else: 
        return who_moved 

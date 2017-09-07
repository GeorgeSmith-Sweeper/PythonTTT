from board import Board

class User:
    current_player = ' ' 

    def __init__(self, symbol):
        self.symbol = symbol
    '''    
    def switch_player(self, player):
        if self.current_player == player:
            current_player = player
        else:
            return None
    '''
def get_input(choice):
    return input(choice)

def spot_choice():
    response = int(get_input("Choose number from 1-9: "))
    return response


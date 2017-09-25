from board import Board, SpotStates 
from ui import Ui, CommandLinePrompt

class User:
    current_player = 'X' 

    def __init__(self, symbol):
        self.symbol = symbol

    def switch_current_user(who_moved, opponent):
        if who_moved == User.current_player:
            User.current_player = opponent
            return User.current_player 

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
            
    def pick_game_mode():
        valid_mode = False
        while valid_mode is False:
            mode = CommandLinePrompt.get_input("Please select a game mode: 1) Human V Human 2) Human V Computer 3) Computer V Computer: ")
            if mode == "1" or mode == "2" or mode == "3":
                valid_mode = True
                return mode

'''
class UserChoice:
    def validate_this_spot(current_state, spot):

        if SpotStates.spot_exists(current_state, spot) is False:
            Ui.msg("That spot is outside of the board range.")
            return False

        if SpotStates.is_occupied(current_state, spot) is False:
            Ui.msg("That spot is occupied. Try again!")
            return False
        
        return True
    
    def check_if_occupied(current_state, spot_choice):
        while SpotStates.is_occupied(current_state, spot_choice)
                Ui.msg("That spot is occupied, please pick again!") 
            else:
                return spot_choice 

    def check_if_spot_exists(current_state, user_spot_choice):
        spot_list = []
        spot_list.extend(range(1, len(current_state) + 1))
        spot_list = list(map(str, spot_list))
        if user_spot_choice not in spot_list:
            raise ValueError
       
    def return_valid_choice(current_state):
        while True:
            user_spot_choice = int(CommandLinePrompt.get_input("Enter a number between 1-9: "))
            try:
                UserChoice.check_if_spot_exists(current_state, user_spot_choice)
                return user_spot_choice 
            except ValueError:
                Ui.msg("That is not a valid spot. Please pick again!")
                self.return_valid_choice(current_state)
'''

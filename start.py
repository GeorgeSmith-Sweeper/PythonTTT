from board import Board, EndStates, SpotStates, BoardState, display_board
from user import User, UserActions, get_input
import board
from ui import Ui

def print_board(current_state):
    Ui.msg(display_board(current_state))

def start_game(current_state, player1, player2):
    print_board(current_state)
    
    if EndStates.is_draw(current_state):
        Ui.msg('DRAW. GameOver')
        return 'DRAW. Game Over'
    
    response = get_input("Enter a number from 1-9: ")
    response = UserActions.make_move(current_state, response)

    if response == False:
        # add error msg
        start_game(current_state, player1, player2)

    # update the board state
    BoardState.update_state(current_state, User.current_player, response)
     
    if User.current_player == player1:
        User.switch_current_user(User.current_player, player2)
        start_game(current_state, player1, player2) 
    else:
        User.switch_current_user(User.current_player, player1)
        start_game(current_state, player1, player2)

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game() 
    player1 = User("X")
    player2 = User("O")
    start_game(game_board.board_state, player1.symbol, player2.symbol)

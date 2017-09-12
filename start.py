from board import Board, is_draw
from user import User, spot_choice, turn_swap, get_input
import board

def print_board():
    print(game_board.display_board())

def start_game(current_state, player1, player2):
    print_board()
    if is_draw(current_state):
        # add ui msg for Draw state
        print('DRAW. Game Over')
        return 'DRAW. Game Over'
    response = get_input("Enter a number from 1-9: ")
    # validate
    response = spot_choice(current_state, response)

    if response == False:
        # add error msg
        start_game(current_state, player1, player2)

    # update the board state
    board.update_state(current_state, User.current_player, response)
     
    if User.current_player == player1:
        turn_swap(User.current_player, player2)
        start_game(current_state, player1, player2) 
    else:
        turn_swap(User.current_player, player1)
        start_game(current_state, player1, player2)

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game() 
    player1 = User("X")
    player2 = User("O")
    start_game(game_board.board_state, player1.symbol, player2.symbol)

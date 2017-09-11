from board import Board, is_draw
from user import User, spot_choice, turn_swap

def print_board():
    print(game_board.display_board())

def continue_turn_prompt(current_state, player1, player2):
    if is_draw(current_state):
        print('DRAW. Game Over')
        return 'DRAW. Game Over'
    else: 
        spot_choice(current_state)
        print_board()
        if (User.current_player == player1):
            turn_swap(User.current_player, player2)
            continue_turn_prompt(current_state, player1, player2)
        else: 
            turn_swap(User.current_player, player1)
            continue_turn_prompt(current_state, player1, player2)
        
if __name__ == "__main__":
    game_board = Board()
    game_board.new_game() 
    player1 = User("X")
    player2 = User("O")
    continue_turn_prompt(game_board.board_state, player1.symbol, player2.symbol)

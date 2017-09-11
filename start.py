from board import Board
from user import User, spot_choice

def print_board():
    print(game_board.display_board())

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game() 
    player1 = User("X")
    player2 = User("O")
    print_board()
    spot_choice(game_board.board_state)
    print_board()

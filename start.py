from board import Board

def print_board_on_start():
    print(game_board.display_board())

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game()
    print_board_on_start()

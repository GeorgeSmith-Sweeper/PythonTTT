from user import User
from board import Board
from start import start_game 

def test_prompt_game_notifies_user_of_a_draw():
    game_board = Board()
    game_board.board_state = [
                                "X", "O", "X", 
                                "O", "X", "O", 
                                "X", "O", "X"
                             ]
    player1 = User("X")
    player2 = User("O")
    assert start_game(game_board.board_state, player1.symbol, player2.symbol) == True 

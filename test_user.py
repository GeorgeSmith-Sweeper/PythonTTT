from board import Board, BoardState
from user import User, UserActions 
from unittest import TestCase
from unittest.mock import patch

# Original version
def test_when_player_is_created_it_has_a_symbol():
    player1 = User("X")
    assert player1.symbol == "X" 

def test_valid_choice_is_returned():
    game_board = Board()
    game_board.new_game()
    assert UserActions.make_move(game_board.board_state, "1") == 1
    
def test_invalid_symbol_returns_false():
    game_board = Board()
    game_board.new_game()
    assert UserActions.make_move(game_board.board_state, "x") == False 
    
def test_invalid_spot_too_large_returns_false():
    game_board = Board()
    game_board.new_game()
    assert UserActions.make_move(game_board.board_state, "12") == False

def test_when_a_user_finishes_move_it_is_the_opponents_turn():
    game_board = Board()
    game_board.new_game()
    BoardState.update_state(game_board.board_state, User.current_player, 1)
    player1 = User("X")
    player2 = User("O")
    User.switch_current_user(User.current_player, player2.symbol)
    assert User.current_player == "O"

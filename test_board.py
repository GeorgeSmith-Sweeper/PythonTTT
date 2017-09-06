import pytest
from board import Board

def test_board_state_is_a_list():
    game_board = Board()
    assert game_board.board_state == []

def test_when_a_user_begins_a_game_a_3X3_board_is_created():
    game_board = Board()
    game_board.new_game()
    assert game_board.board_state == [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def test_when_a_user_supplies_4_rows_a_4x4_board_is_created():
    game_board = Board()
    game_board.new_game(4)
    assert game_board.board_state == [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# must test 'sad' path for new_game by passing in a value less then 3

def test_when_a_user_picks_a_spot_board_is_displayed_with_their_symbol_at_spot():
    game_board = Board()
    player1 = 'X'
    spot = 1
    game_board.new_game()
    game_board.update_state(game_board.board_state, player1, spot)
    assert game_board.board_state == ["X", " ", " ", " ", " ", " ", " ", " ", " "]

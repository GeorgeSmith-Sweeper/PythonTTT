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
'''
def test_update_state_can_modify_board_state():
    game_board = Board()
    game_board.update_state()
'''

import pytest
from board import Board

def test_board_state_is_a_list():
    game_board = Board()
    assert game_board.board_state == []
    '''
    assert game_board.grid == [" ", " ", " ", " ", " ", " ", " ", " "]
    '''

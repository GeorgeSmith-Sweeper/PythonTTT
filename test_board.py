import pytest
from board import Board, spot_exists

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

def test_when_a_user_picks_a_spot_board_is_updated_with_their_spot():
    game_board = Board()
    player1 = 'X'
    spot = 1
    game_board.new_game()
    game_board.update_state(game_board.board_state, player1, spot)
    assert game_board.board_state == ["X", " ", " ", " ", " ", " ", " ", " ", " "]

def test_when_a_user_picks_a_spot_smaller_then_exists_spot_exists_is_False():
    game_board = Board()
    spot = -1
    game_board.new_game()
    assert spot_exists(game_board.board_state, spot) == False

def test_when_a_user_picks_a_spot_larger_then_exists_spot_exists_is_False():
    game_board = Board()
    game_board.new_game()
    spot = len(game_board.board_state) 
    assert spot_exists(game_board.board_state, spot) == False

def test_when_a_user_picks_a_spot_that_exists_spot_exists_is_True():
    game_board = Board()
    game_board.new_game()
    spot = 1 
    assert spot_exists(game_board.board_state, spot) == True
'''    
def test_when_a_user_picks_an_occupied_spot_is_occupied_will_be_True():
    game_board = Board()
    spot = 1
    player1 = 'X'
    game_board.new_game()
    game_board.update_state(game_board.board_state, player1, spot)
    assert game_board.is_occupied(game_board.board_state, spot) == True

def test_current_board_is_displayed():
    game_board = Board()
    game_board.new_game()
    assert game_board.display_board() == game_board.board_state[0] + " | " + game_board.board_state[1] + " | " + game_board.board_state[2] + "\n" +"=========" + "\n" + game_board.board_state[3] + " | " + game_board.board_state[4] + " | " + game_board.board_state[5] + "\n" + "=========" + "\n" + game_board.board_state[6] + " | " + game_board.board_state[7] + " | " + game_board.board_state[8] 
'''

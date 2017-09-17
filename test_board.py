import pytest
import board
from board import Board, EndStates, SpotStates, BoardState, WinningCombos, display_board

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
    BoardState.update_state(game_board.board_state, player1, spot)
    assert game_board.board_state == ["X", " ", " ", " ", " ", " ", " ", " ", " "]

def test_when_a_user_picks_a_spot_smaller_then_exists_spot_exists_is_False():
    game_board = Board()
    spot = -1
    game_board.new_game()
    assert SpotStates.spot_exists(game_board.board_state, spot) == False

def test_when_a_user_picks_a_spot_larger_then_exists_spot_exists_is_False():
    game_board = Board()
    game_board.new_game()
    spot = len(game_board.board_state) + 1 
    assert SpotStates.spot_exists(game_board.board_state, spot) == False

def test_when_a_user_picks_a_spot_that_exists_spot_exists_is_True():
    game_board = Board()
    game_board.new_game()
    spot = 1 
    assert SpotStates.spot_exists(game_board.board_state, spot) == True
    
def test_when_a_user_picks_an_occupied_spot_is_occupied_will_be_True():
    game_board = Board()
    spot = 1
    player1 = 'X'
    game_board.new_game()
    BoardState.update_state(game_board.board_state, player1, spot)
    assert SpotStates.is_occupied(game_board.board_state, spot) == True

def test_game_ends_when_board_is_full():
    game_board = Board()
    game_board.board_state = ["X","O","X","O","X","O","X","O","O"]
    assert EndStates.is_draw(game_board.board_state) == True

def test_game_continues_if_board_is_not_full():
    game_board = Board()
    game_board.board_state = ["O","O"," ","O","X","O","X","O","O"]
    assert EndStates.is_draw(game_board.board_state) == False 
    
def test_win_by_row_returns_possible_row_wins():
    win_config = WinningCombos(3)
    win_config.win_by_row() == [
                                [0, 1, 2], 
                                [3, 4, 5], 
                                [6, 7, 8]
                                ]

def test_win_by_column_returns_possible_column_wins():
    win_config = WinningCombos(3)
    win_config.win_by_column(win_config.win_by_row()) == [
                                                            [0, 3, 6], 
                                                            [1, 4, 7], 
                                                            [2, 5, 8]
                                                         ]
def test_winning_combos_are_created_for_3x3_board():
    win_config = WinningCombos(3)
    win_config.create_winning_combos()
    assert win_config.winning_combos == [
                                         [0, 1, 2],
                                         [3, 4, 5],
                                         [6, 7, 8],
                                         [0, 3, 6],
                                         [1, 4, 7],
                                         [2, 5, 8],
                                         [0, 4, 8],
                                         [2, 4, 6],
                                        ]
def test_current_board_is_displayed():
    game_board = Board()
    game_board.new_game()
    assert display_board(game_board.board_state) == game_board.board_state[0] + " | " + game_board.board_state[1] + " | " + game_board.board_state[2] + "\n" +"=========" + "\n" + game_board.board_state[3] + " | " + game_board.board_state[4] + " | " + game_board.board_state[5] + "\n" + "=========" + "\n" + game_board.board_state[6] + " | " + game_board.board_state[7] + " | " + game_board.board_state[8] 


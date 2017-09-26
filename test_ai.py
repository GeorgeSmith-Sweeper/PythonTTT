from board import BoardState, Board
from ai import Ai

def test_Ai_only_selects_an_empty_spot_on_board():
   game_board = Board()
   game_board.board_state = [
                                "O", "O", "X",
                                "X", "O", "O",
                                "", "X", "X",
                             ]
   assert Ai.make_move(game_board.board_state) == 7 
                                                                   
def test_Ai_makes_no_move_if_board_is_full():
   game_board = Board()
   game_board.board_state = [
                                "O", "O", "X",
                                "X", "O", "O",
                                "X", "X", "X",
                             ]
   assert Ai.make_move(game_board.board_state) == None 
   
def test_Ai_only_makes_one_move_():
   game_board = Board()
   game_board.board_state = [
                                "", "", "",
                                "X", "O", "O",
                                "X", "X", "X",
                             ]
   assert Ai.make_move(game_board.board_state) == 1 

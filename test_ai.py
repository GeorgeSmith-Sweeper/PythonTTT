from board import BoardState, Board
from ai import Ai

def test_Ai_only_selects_an_empty_spot_on_board():
   game_board = Board()
   game_board.board_state = [
                                "O", "O", "X",
                                "X", "O", "O",
                                "", "X", "X",
                             ]
   current_player = 'X'
   assert Ai.make_move(game_board.board_state, current_player) ==  [ 
                                                                    "O", "O", "X",
                                                                    "X", "O", "O",
                                                                    "X", "X", "X",
                                                                   ]
def test_Ai_makes_no_move_if_board_is_full():
   game_board = Board()
   game_board.board_state = [
                                "O", "O", "X",
                                "X", "O", "O",
                                "X", "X", "X",
                             ]
   current_player = 'X'
   assert Ai.make_move(game_board.board_state, current_player) ==  [ 
                                                                    "O", "O", "X",
                                                                    "X", "O", "O",
                                                                    "X", "X", "X",
                                                                   ]

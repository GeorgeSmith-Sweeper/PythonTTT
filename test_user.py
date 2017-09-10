from board import Board
from unittest.mock import patch
from unittest import TestCase
from user import User, spot_choice 

def test_when_player_is_created_it_has_a_symbol():
    player1 = User("X")
    assert player1.symbol == "X" 

class TestUserInputs(TestCase):
    @patch('user.get_input', return_value='1')
    def test_can_receive_user_input(self, input):
        game_board = Board()
        game_board.new_game()
        self.assertEqual(spot_choice(game_board.board_state), 1)
'''
    @patch('user.get_input', return_value='x')
    def test_if_users_move_is_not_a_number_return_false(self, input):
        game_board = Board()
        game_board.new_game()
        self.assertEqual(spot_choice(), False) 
'''

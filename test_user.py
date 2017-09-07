from unittest.mock import patch
from unittest import TestCase
from user import User, spot_choice 

def test_when_player_is_created_it_has_a_symbol():
    player1 = User("X")
    assert player1.symbol == "X" 

class TestUserInputs(TestCase):
    @patch('user.get_input', return_value=1)
    def test_can_receive_user_input(self, input):
        self.assertEqual(spot_choice(), 1)
'''
    @patch('user.get_input', return_value=1)
    def test_if_users_move_is_a_num_rtrn_True(self, input):
        self.assertEqual(spot_choice_is_num(), True) 
'''

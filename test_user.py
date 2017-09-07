from unittest.mock import patch
from unittest import TestCase
from user import User, spot_choice

def test_when_player_is_created_it_has_a_symbol():
    player1 = User("X")
    assert player1.symbol == "X" 

class Test(TestCase):
    @patch('user.get_input', return_value=1)
    def test_answer_1(self, input):
        self.assertEqual(spot_choice(), 1) 

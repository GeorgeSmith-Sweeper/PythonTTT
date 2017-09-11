from board import Board, update_state
from unittest.mock import patch
from unittest import TestCase
from user import User, spot_choice, turn_swap 

def test_when_player_is_created_it_has_a_symbol():
    player1 = User("X")
    assert player1.symbol == "X" 

class TestUserInputs(TestCase):
    @patch('user.get_input', return_value='1')
    def test_users_choice_updates_game_board(self, input):
        game_board = Board()
        game_board.new_game()
        self.assertEqual(spot_choice(game_board.board_state), 1)

    @patch('user.get_input', return_value='x')
    def test_user_choice_returns_invalid_if_user_inputs_an_invalid_symbol(self, input):
        game_board = Board()
        game_board.new_game()
        self.assertEqual(spot_choice(game_board.board_state), 'invalid choice') 
    
    @patch('user.get_input', return_value='2')
    def test_user_choice_returns_invalid_if_user_inputs_an_invalid_symbol(self, input):
        game_board = Board()
        game_board.new_game()
        update_state(game_board.board_state, "X", 2)
        self.assertEqual(spot_choice(game_board.board_state), 'spot is occupied') 

def test_when_a_user_finishes_move_it_is_the_opponents_turn():
    game_board = Board()
    game_board.new_game()
    update_state(game_board.board_state, User.current_player, 1)
    player1 = User("X")
    player2 = User("O")
    turn_swap(User.current_player, player2.symbol)
    assert User.current_player == "O"

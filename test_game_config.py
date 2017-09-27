from unittest.mock import patch
from unittest import TestCase
import pytest
from game_config import GameModePrompt, ModeValidation, GameConfig
import ui

class TestUserModeSelection(TestCase):
    @patch('ui.CommandLinePrompt.get_input', return_value='1')
    def test_a_users_selection_is_returned(self, input):
        game_mode_config = GameModePrompt()
        self.assertEqual(game_mode_config.ask_user_for_mode(), '1')

    @patch('game_config.GameModePrompt.ask_user_for_mode', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = ModeValidation("1")
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')

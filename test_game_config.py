from unittest.mock import patch
from unittest import TestCase
import pytest
from game_config import GameModePrompt, ModeValidation, GameConfig
import ui

class TestUserModeSelection(TestCase):
    @patch('game_config.GameModePrompt.ask_user_for_mode', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = ModeValidation("1")
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')

from unittest.mock import patch
from unittest import TestCase
import pytest
from game_config import GameModePrompt, LanguageModePrompt, GameModeValidation, LanguageModeValidation,  GameConfig 
import ui

class TestUserModeSelection(TestCase):
    
    @patch('game_config.GameModePrompt.ask_user_questions', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = GameModeValidation('1')
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')
    
    @patch('ui.CommandLinePrompt.get_input', return_value='1')
    def test_a_players_selection_is_returned(self, input):
        self.assertEqual(GameModePrompt.ask_user_questions(), '1')
    
def test_an_invalid_selection_returns_ValueError():
    mode_choice = GameModeValidation('4')
    with pytest.raises(ValueError):
        mode_choice.validate()

class TestUserLanguageSelection(TestCase):
    
    @patch('game_config.LanguageModePrompt.ask_user_questions', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = LanguageModeValidation('1')
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')
    
    @patch('ui.CommandLinePrompt.get_input', return_value='1')
    def test_a_players_selection_is_returned(self, input):
        self.assertEqual(LanguageModePrompt.ask_user_questions(), '1')
    
def test_an_invalid_selection_returns_ValueError():
    mode_choice = LanguageModeValidation('4')
    with pytest.raises(ValueError):
        mode_choice.validate()

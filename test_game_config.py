from unittest.mock import patch
from unittest import TestCase
import pytest
from ui import LANGUAGE_MODE_STRING, GAME_MODE_STRING
from game_config import SetUpPrompts, config

class TestUserLanguageSelection(TestCase):    
    @patch('ui.CommandLinePrompt.get_input', return_value='2')
    def test_a_players_selection_is_returned(self, input):
        options = {
                'question': { 
                    'Language': LANGUAGE_MODE_STRING,
                    },
                'valid_choices': {
                    'Language': ['1', '2'],
                    }
                }
        setup = SetUpPrompts()
        setup.run_set_up(options)
        self.assertEqual(config["Language"], '2')

class TestUserLanguageSelection(TestCase):    
    @patch('ui.CommandLinePrompt.get_input', return_value='2')
    def test_a_players_selection_is_returned(self, input):
        options = {
                'question': { 
                    'Language': LANGUAGE_MODE_STRING,
                    'Game_Mode': GAME_MODE_STRING,
                    },
                'valid_choices': {
                    'Language': ['1', '2'],
                    'Game_Mode': ['1', '2', '3'],
                    }
                }
        setup = SetUpPrompts()
        setup.run_set_up(options)
        self.assertEqual(config["Game_Mode"], '2')

'''
    @patch('ui.CommandLinePrompt.get_input', return_value='1') 
    def test_the_users_input_is_returned_if_selection_is_valid(self, input):
        setup = SetUpPrompts()
        response = setup.ask_user_questions(LanguageModeOptions)
        self.assertEqual(setup.validate_choice(response), '1')
from game_config import GameModePrompt, LanguageModePrompt, GameModeValidation, LanguageModeValidation,  GameConfig 
class TestUserModeSelection(TestCase):
    
    @patch('game_config.GameModePrompt.ask_user_questions', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = GameModeValidation('1')
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')
    
    @patch('ui.CommandLinePrompt.get_input', return_value='1')
    def test_a_players_selection_is_returned(self, input):
        self.assertEqual(GameModePrompt.ask_user_questions(), '1')
    
def test_an_invalid_selection_returns_False():
    mode_choice = GameModeValidation('4')
    mode_choice.validate() == False

class TestUserLanguageSelection(TestCase):
    
    @patch('game_config.LanguageModePrompt.ask_user_questions', return_value='1')
    def test_a_valid_mode_is_stored(self, input):
        mode_choice = LanguageModeValidation('1')
        mode_choice.validate()
        self.assertEqual(GameConfig.mode, '1')
    
    @patch('ui.CommandLinePrompt.get_input', return_value='1')
    def test_a_players_selection_is_returned(self, input):
        self.assertEqual(LanguageModePrompt.ask_user_questions(), '1')
    
def test_an_invalid_selection_returns_False():
    mode_choice = LanguageModeValidation('4')
    mode_choice.validate() == False

'''

from unittest.mock import patch
from unittest import TestCase
import pytest
from ui import LANGUAGE_MODE_STRING, GAME_MODE_STRING, PLAYER1_SYMBOL_STRING, PLAYER2_SYMBOL_STRING
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

class TestUserLanguageAndModeSelection(TestCase):    
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

class TestPlayersSymbolChoice(TestCase):    
    @patch('ui.CommandLinePrompt.get_input', return_value='X')
    def test_a_players_selection_is_returned(self, input):
        options = {
                'question': { 
                    'Player1_Symbol': PLAYER1_SYMBOL_STRING,
                    },
                'valid_choices': {
                    'Player1_Symbol': ['X','O'],
                    }
                }
        setup = SetUpPrompts()
        setup.run_set_up(options)
        self.assertEqual(config["Player1_Symbol"], 'X')

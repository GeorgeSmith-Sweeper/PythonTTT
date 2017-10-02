from unittest.mock import patch
from unittest import TestCase
import pytest
from ui import LANGUAGE_MODE_STRING, GAME_MODE_STRING, PLAYER1_SYMBOL_STRING, PLAYER2_SYMBOL_STRING
from game_config import SetUpPrompts, SymbolPrompts, config 

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

class TestUserSymbolSelection(TestCase):    
    @patch('ui.CommandLinePrompt.get_input', return_value='W')
    def test_a_players_selection_is_returned(self, input):
        setup = {
            'Player1': PLAYER1_SYMBOL_STRING
            }
        setup_symbols = SymbolPrompts()
        setup_symbols.gather_symbols(setup)
        self.assertEqual(config['Player1'], 'W')

def test_users_symbol_is_only_returned_if_legal(): 
    setup = SymbolPrompts()
    symbol = 'X'
    assert setup.validate_user_symbol(symbol) == 'X'

def test_users_symbol_can_not_be_a_space():
    setup = SymbolPrompts()
    symbol = ' '
    assert setup.validate_user_symbol(symbol) == False 

def test_users_symbol_can_only_be_one_char():
    setup = SymbolPrompts()
    symbol = 'asdf'
    assert setup.validate_user_symbol(symbol) == False 

def test_users_symbol_can_not_be_blank():
    setup = SymbolPrompts()
    symbol = ''
    assert setup.validate_user_symbol(symbol) == False 




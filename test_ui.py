import pytest
from ui import Ui, GameModeOptions, LanguageModeOptions
from unittest.mock import patch
from unittest import TestCase


def test_ui_display_takes_a_string_and_returns_it():
        assert Ui.msg("Oh nooo") == print("Oh nooo")

def test_game_mode_options_displays_three_options_when_called():
    options_string = ("\n"
                      "Please select from the following game modes" 
                      "\n"
                      "1) Human Vs Human"
                      "\n"
                      "2) Human Vs Computer"
                      "\n"
                      "3) Computer Vs Computer"
                      "\n"
                     )

    GameModeOptions.show_options == options_string 


def test_language_options_gives_a_choice_btwn_french_and_english():
    options_string = ("\n"
                      "Would you like play in English or French?" 
                      "\n"
                      "1) English"
                      "\n"
                      "2) French"
                      "\n"
                     )
    LanguageModeOptions.show_options == options_string


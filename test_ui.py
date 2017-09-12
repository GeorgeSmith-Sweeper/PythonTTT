import pytest
from ui import Ui

def test_ui_display_takes_a_string_and_returns_it():
    assert Ui.msg("Oh nooo") == "Oh nooo"

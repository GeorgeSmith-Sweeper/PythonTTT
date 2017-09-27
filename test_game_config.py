from unittest.mock import patch
from unittest import TestCase
import pytest
from game_config import GameModeSelection

def test_a_users_selection_is_returned():
    mode_choice = GameModeSelection()
    assert mode_choice.ask_user_for_mode() == "1"


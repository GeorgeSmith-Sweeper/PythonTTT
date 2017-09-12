import pytest
from ui import Ui
from board import Board, update_state
from unittest.mock import patch
from unittest import TestCase


def test_ui_display_takes_a_string_and_returns_it():
    assert Ui.msg("Oh nooo") == print("Oh nooo")

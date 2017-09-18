import pytest
from ui import Ui, BoardPresenter
from unittest.mock import patch
from unittest import TestCase


def test_ui_display_takes_a_string_and_returns_it():
    assert Ui.msg("Oh nooo") == print("Oh nooo")

'''
def test_user_is_displayed_a_3x3_grid_with_place_holders():
    current_board_state = [
                            "", "", "",
                            "", "", "",
                            "", "", "",
                          ]
    assert BoardPresenter.display_terminal_board(current_board_state) == '1 | 2 | 3' + '\n' +
                                                                         '_________' + '\n' +
                                                                         '4 | 5 | 6' + '\n' +
                                                                         '_________' + '\n' +
                                                                         '7 | 8 | 9'
'''

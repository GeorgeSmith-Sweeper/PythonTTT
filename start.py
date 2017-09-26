from board import Board, EndStates, SpotStates, BoardState, WinningCombos 
from user import User, UserActions 
import board
from ui import Ui, BoardPresenter, CommandLinePrompt

def begin_game(mode_choosen, current_state, player1, player2):
    if mode_choosen == "1":
        human_v_human(current_state, player1, player2)
    if mode_choosen == "2":
        human_v_computer()
    if mode_choosen == "3":
        computer_v_computer()

def human_v_computer():
    Ui.msg("you can get here but nothing happens")
    return None

def computer_v_computer():
    Ui.msg("you can get here but nothing happens")
    return None


def human_v_human(current_state, player1, player2):
    game_over = False
    while game_over is False:
        response = False
        while response is False:
            Ui.msg(BoardPresenter.display_terminal_board(current_state))
            response = CommandLinePrompt.get_input("Enter a number from 1-9: ") 
            response = UserActions.make_move(current_state, response)
        BoardState.update_state(current_state, User.current_player, response)
        if EndStates.did_a_player_win(current_state, User.current_player, win_config.winning_combos):
            Ui.msg(BoardPresenter.display_terminal_board(current_state)) 
            Ui.msg('Game Over: ' + User.current_player + ' WINS!')
            return True
        if EndStates.is_draw(current_state):
            Ui.msg('DRAW. GameOver')
            return True
        if User.current_player == player1:
            User.switch_current_user(User.current_player, player2)
        else:
            User.switch_current_user(User.current_player, player1)
        
'''
def human_v_human(current_state, player1, player2):
     
    Ui.msg(BoardPresenter.display_terminal_board(current_state))
    response = CommandLinePrompt.get_input("Enter a number from 1-9: ") 
    response = UserActions.make_move(current_state, response)
     
    if response == False:
        human_v_human(current_state, player1, player2)
    BoardState.update_state(current_state, User.current_player, response)

    if EndStates.did_a_player_win(current_state, User.current_player, win_config.winning_combos):
        Ui.msg(BoardPresenter.display_terminal_board(current_state)) 
        Ui.msg('Game Over: ' + User.current_player + ' WINS!')
        return True
    if EndStates.is_draw(current_state):
        Ui.msg('DRAW. GameOver')
        return True
     
    if User.current_player == player1:
        User.switch_current_user(User.current_player, player2)
    else:
        User.switch_current_user(User.current_player, player1)
    human_v_human(current_state, player1, player2)
'''

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game(3) 
    win_config = WinningCombos(3)
    win_config.create_winning_combos()
    player1 = User("X")
    player2 = User("O")
    mode_choice = UserActions.pick_game_mode()
    begin_game(mode_choice, game_board.board_state, player1.symbol, player2.symbol)

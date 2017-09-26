from board import Board, EndStates, SpotStates, BoardState, WinningCombos
from user import User, UserActions
from ai import Ai
import board
from ui import Ui, BoardPresenter, CommandLinePrompt

class GameModes:
    def human_v_computer(current_state, player1, player2):
        game_over = False

        while game_over is False:
            if User.current_player == player2:
                Ui.msg("Computer has moved")
                computers_move = Ai.make_move(current_state)
                BoardState.update_state(current_state, User.current_player, computers_move)
                if User.current_player == player1:
                    User.switch_current_user(User.current_player, player2)
                User.switch_current_user(User.current_player, player1)
            else:
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

    def computer_v_computer(current_state, player1, player2):
        game_over = False
        while game_over is False:
                Ui.msg(BoardPresenter.display_terminal_board(current_state))
                computers_move = Ai.make_move(current_state)
                BoardState.update_state(current_state, User.current_player, computers_move)
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

def begin_game(mode_choosen, current_state, player1, player2):
    if mode_choosen == "1":
        GameModes.human_v_human(current_state, player1, player2)
    if mode_choosen == "2":
        GameModes.human_v_computer(current_state, player1, player2)
    if mode_choosen == "3":
        GameModes.computer_v_computer(current_state, player1, player2)

if __name__ == "__main__":
    game_board = Board()
    game_board.new_game(3)
    win_config = WinningCombos(3)
    win_config.create_winning_combos()
    player1 = User("X")
    player2 = User("O")
    mode_choice = UserActions.pick_game_mode()
    begin_game(mode_choice, game_board.board_state, player1.symbol, player2.symbol)

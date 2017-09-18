import math

class Ui:
    def msg(message):
        print(message)
    
class BoardPresenter:
    def display_terminal_board(current_board_state):
        cbs = current_board_state
        num_rows = math.sqrt(len(cbs))
        pipe = ' | '
        divider = "_________"
        row_holder = []
        full_board = []

        for spot in range(0, len(cbs)):
            if cbs[spot] == "":
                row_holder.append(str(spot + 1))
            else:
                row_holder.append(cbs[spot])
            row_holder.append(pipe)
            if len(row_holder) == (num_rows * 2):
                row_holder.pop()
                full_board.append(''.join(row_holder) + '\n')
                full_board.append(divider + '\n')
                row_holder = []
        full_board.pop()
        full_board = ''.join(full_board)
        return full_board
'''
Ui.msg(BoardPresenter.display_terminal_board(["X", "O", "", "", "X", "", "", "", "",]))
'''

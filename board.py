class Board:
    board_state = []
   
    def new_game(self, numrows=3):
        board_area = numrows*numrows
        new_board = [" "] * board_area
        self.board_state = new_board

# All possible ways a game can end
class EndStates:
    def win_by_row():
        return None

    def win_by_column():
        return None

    def win_by_diagonal():
        return None

    def is_draw(current_state):
        return  " " not in current_state

class SpotStates:
    def spot_exists(current_state, spot):
        return (spot - 1) >= 0 and spot <= len(current_state)

    def is_occupied(current_state, spot):
       return current_state[spot - 1] != " "

class BoardState:
    def update_state(current_state, player_symbol, spot):
        new_state = current_state
        new_state[spot - 1] = player_symbol
        Board.board_state = new_state 


def display_board(current_state):
    return current_state[0] + " | " + current_state[1] + " | " + current_state[2] + "\n" +"=========" + "\n" + current_state[3] + " | " + current_state[4] + " | " + current_state[5] + "\n" + "=========" + "\n" + current_state[6] + " | " + current_state[7] + " | " + current_state[8]

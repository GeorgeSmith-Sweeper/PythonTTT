from board import BoardState, Board

class Ai:
    def make_move(current_board_state):
        new_state = current_board_state
        for spot in range(0, len(new_state)):
            if new_state[spot] == "":
                return spot + 1
        return None

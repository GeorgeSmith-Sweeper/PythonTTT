from board import BoardState, Board

class Ai:
    def make_move(current_board_state, current_player):
        new_state = current_board_state
        for spot in range(0, len(new_state)):
            if new_state[spot] == "":
                new_state[spot] = current_player
                return new_state
        return new_state

class Board:
    def __init__(self):
        self.board_state = []

    def update_state(self, current_state, player, spotchoice):
        new_state = current_state
        new_state[spotchoice - 1] = player
        self.board_state = new_state

    def new_game(self, numrows=3):
        board_area = numrows*numrows
        new_board = [" "] * board_area
        self.board_state = new_board

    def is_occupied(self, current_state, spotChoice):
        if current_state[spotChoice - 1] != " ":
            return True
        else:
            return False

    def display_board(self):
        return self.board_state[0] + " | " + self.board_state[1] + " | " + self.board_state[2] + "\n" +"=========" + "\n" + self.board_state[3] + " | " + self.board_state[4] + " | " + self.board_state[5] + "\n" + "=========" + "\n" + self.board_state[6] + " | " + self.board_state[7] + " | " + self.board_state[8]

def spot_exists(current_state, spotChoice):
    if (spotChoice - 1) >= 0 and spotChoice < len(current_state):
        return True
    else:
        return False

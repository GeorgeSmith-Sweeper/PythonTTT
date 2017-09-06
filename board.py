class Board:
    def __init__(self):
        self.board_state = []

    def update_state(self, current_state, player, spotChoice):
        new_state = current_state
        new_state[spotChoice - 1] = player
        self.board_state = new_state
    
    def new_game(self, numRows=3):
        board_area = numRows*numRows
        new_board = [" "] * board_area
        self.board_state = new_board 

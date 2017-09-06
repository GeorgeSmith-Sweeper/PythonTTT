class Board:
    def __init__(self):
        self.board_state = []

    def update_state(self, new_state):
        self.board_state = new_state
    
    def new_game(self, numRows=3):
        board_area = numRows*numRows
        new_board = [" "] * board_area
        self.update_state(new_board)

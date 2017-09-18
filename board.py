class Board:
    def __init__(self):
        self.board_state = []

    def new_game(self, numrows=3):
        board_area = numrows*numrows
        new_board = [""] * board_area
        self.board_state = new_board

# All possible ways a game can end
class WinningCombos:
    def __init__(self, size):
        self.size = size
        self.winning_combos = []

    def win_by_row(self):
        winning_rows = []
        single_row = []
        for spot in range(0, self.size*self.size):
            single_row.append(spot)
            if len(single_row) == self.size:
                winning_rows.append(single_row)
                single_row = []
        return winning_rows

    def win_by_column(self, rows):
        winning_columns = []
        for outer in range(0, self.size):
            single_column = []
            for inner in range(0, self.size):
                single_column.append(rows[inner][outer])
            winning_columns.append(single_column)
        return winning_columns

    def diagonal_left_to_right_win(self, rows):
        left_to_right = []
        for spot in range(0, self.size):
            left_to_right.append(rows[spot][spot])
        return left_to_right
    
    def diagonal_right_to_left_win(self, rows):
        right_to_left = []
        size = self.size
        spot = size
        while spot > 0:
            right_to_left.append(rows[spot - 1][size - spot])
            spot -= 1
        right_to_left.reverse()
        return right_to_left
    
    def create_winning_combos(self):        
        winning_rows = self.win_by_row()
        winning_columns = self.win_by_column(winning_rows)
        diagonal_left_to_right = self.diagonal_left_to_right_win(winning_rows)
        diagonal_right_to_left = self.diagonal_right_to_left_win(winning_rows)

        for row in winning_rows:
            self.winning_combos.append(row)
        
        for column in winning_columns:
            self.winning_combos.append(column)
        
        self.winning_combos.append(diagonal_left_to_right) 
        self.winning_combos.append(diagonal_right_to_left) 

class EndStates:
    def is_draw(current_state):
        return  "" not in current_state

    def did_a_player_win(current_state, current_player, win_combos):
        # loop through combos list 
        for spot_list in range(0, len(win_combos)):
            win = True
            for spot in range(0, (int(len(win_combos) / 2)) - 1):
                if current_state[win_combos[spot_list][spot]] != current_player:
                    win = False 
            if win:
                return True
        return False
        
class SpotStates:
    def spot_exists(current_state, spot):
        return (spot - 1) >= 0 and spot <= len(current_state)

    def is_occupied(current_state, spot):
       return current_state[spot - 1] != ""

class BoardState:
    def update_state(current_state, player_symbol, spot):
        new_state = current_state
        new_state[spot - 1] = player_symbol
        Board.board_state = new_state 

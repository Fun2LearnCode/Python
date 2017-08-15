class InnerGrid:
    def __init__(self, board):
        self.board = board
        self.starting_board = board
    def get_row(self, row_number):
        return self.board[row_number]
    def get_column(self, column_number):
        return [self.board[column_number][0],self.board[column_number][1],self.board[column_number][2]]
    def set_point(self, r, c, value):
        if self.starting_board[r][c] == -1:
            self.board[r][c] = value
    def check_repeating(self):
        values = []
        for row in self.board:
            for value in row:
                if value == -1 or value in values:
                    return True;
                else:
                    values.extend(value);
        return False
    def reset(self):
        self.board = self.starting_board

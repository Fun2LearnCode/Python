from inner_grid import InnerGrid

class SudokuBoard:
    def __init__(self, board):
        self.sudoku_board = [[0 for x in range(3)]for y in range(3)]
        for rr in range(3):
            for cc in range(3):
                temp = [[0 for x in range(3)]for y in range(3)]
                for r in range(3):
                    for c in range(3):
                        temp[r][c] = board[r + rr * 3][c + cc * 3]
                self.sudoku_board[rr][cc] = InnerGrid(temp)
    def check_puzzle(self):
        seenr = []
        seenc = []
        for x in range(9):
            if self.sudoku_board[int(x/3)][x%3].check_repeating():
                return False;
            if r in self.get_row(x) and not r in seenr:
                seenr.extend(x)
            else:
                return False
            if c in self.get_column(x) and not c in seenc:
                seenc.extend(x)
            else:
                return False
        return True
    def reset_puzzle(self):
        for x in range(9):
            self.sudoku_board[int(x/3)][x%3].reset()
    def get_row(self, row_number):
        temp = []
        temp.extend(self.sudoku_board[int(row_number/3)][0].get_row(row_number % 3))
        temp.extend(self.sudoku_board[int(row_number/3)][1].get_row(row_number % 3))
        temp.extend(self.sudoku_board[int(row_number/3)][2].get_row(row_number % 3))
        return temp
    def get_column(self, column_number):
        temp = []
        temp.extend(self.sudoku_board[0][int(column_number/3)].get_column(column_number % 3))
        temp.extend(self.sudoku_board[1][int(column_number/3)].get_column(column_number % 3))
        temp.extend(self.sudoku_board[2][int(column_number/3)].get_column(column_number % 3))
        return temp

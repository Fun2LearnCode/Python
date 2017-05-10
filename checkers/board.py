import Enums
board = [[0 for x in range(7)] for y in range(7)]
for x in range(7):
    for y in range(7):
        if((x % 2 == 0) and (y % 2 == 0)):
            board[x][y] = Enums.Type.RED
            if(x < 4):
                board[x][y] = Enums.Type.RED_PAWN

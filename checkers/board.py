import enums
from piece import Piece
from  tkinter import *
tk = Tk()
board = [[[0 for x in range(8)]for y in range(8)] for z in range(2)]
global_x = -1
global_y = -1
def valid_move(x, y):
    global global_y
    global global_x
    if(board[1][global_y][global_x] == enums.Type.BLACK_KING):
        if(abs(y-global_y) == 1 and abs(global_x-x) == 1 and board[1][y][x] == 0):
            board[1][y][x] = board[1][global_y][global_x]
            create_piece(board[0][y][x], "black")
            board[0][global_y][global_x].delete("all")
            return True
    elif(board[1][global_y][global_x] == enums.Type.RED_KING):
        if(abs(y-global_y) == 1 and abs(global_x-x) == 1 and board[1][y][x] == 0):
            board[1][y][x] = board[1][global_y][global_x]
            create_piece(board[0][y][x], "black")
            board[0][global_y][global_x].delete("all")
            return True

    elif(board[1][global_y][global_x] == enums.Type.BLACK_PAWN):
        if(global_y < y):
            if((y-global_y) == 1 and abs(global_x-x) == 1 and board[1][y][x] == 0):
                board[1][y][x] = board[1][global_y][global_x]
                create_piece(board[0][y][x], "black")
                board[0][global_y][global_x].delete("all")
                return True
            elif((y-global_y) == 2 and abs(global_x-x) == 2):
                if(global_x - x == 2): #if its on the left
                    if(board[1][global_y-1][global_x-1] == enums.Type.RED_PAWN or enums.Type.RED_KING):
                        board[1][y][x] = board[1][global_y][global_x]
                        create_piece(board[0][y][x], "black")
                        board[0][global_y][global_x].delete("all")
                        board[0][global_y+1][global_x-1].delete("all")
                        board[1][global_y+1][global_x-1] = 0
                        return True
                    else:
                        return False
                elif(global_x - x == -2):
                    if(board[1][global_y-1][global_x+1] == enums.Type.RED_PAWN or enums.Type.RED_KING):
                        board[1][y][x] = board[1][global_y][global_x]
                        create_piece(board[0][y][x], "black")
                        board[0][global_y][global_x].delete("all")
                        board[0][global_y+1][global_x+1].delete("all")
                        board[1][global_y+1][global_x+1] = 0
                        return True


    elif(board[1][global_y][global_x] == enums.Type.RED_PAWN):
        if(global_y > y):
            if((global_y-y) == 1 and abs(global_x-x) == 1 and board[1][y][x] == 0):
                board[1][y][x] = board[1][global_y][global_x]
                create_piece(board[0][y][x], "red")
                board[0][global_y][global_x].delete("all")
                return True
            elif((global_y-y) == 2 and abs(global_x-x) == 2):
                if(global_x - x == 2): #if its on the left
                    if(board[1][global_y-1][global_x-1] == enums.Type.BLACK_PAWN or enums.Type.BLACK_KING):
                        board[1][y][x] = board[1][global_y][global_x]
                        create_piece(board[0][y][x], "red")
                        board[0][global_y][global_x].delete("all")
                        board[0][global_y-1][global_x-1].delete("all")
                        board[1][global_y-1][global_x-1] = 0
                        return True
                    else:
                        return False
                elif(global_x - x == -2):
                    if(board[1][global_y-1][global_x+1] == enums.Type.BLACK_PAWN or enums.Type.BLACK_KING):
                        board[1][y][x] = board[1][global_y][global_x]
                        create_piece(board[0][y][x], "red")
                        board[0][global_y][global_x].delete("all")
                        board[0][global_y-1][global_x+1].delete("all")
                        board[1][global_y-1][global_x+1] = 0
                        return True

def click(event):
    global global_y
    global global_x
    x = int((tk.winfo_pointerx() - tk.winfo_rootx())/80)
    y = int((tk.winfo_pointery() - tk.winfo_rooty())/80)
    if(board[0][y][x]["background"] == "black"):
        if(global_x == -1 and global_y == -1): #no piece is selected
            if(board[1][y][x] != 0): #if there is a piece there
                board[0][y][x]["background"] = "blue"
                global_x = x
                global_y = y
        else:
            if(board[1][y][x] != 0):
                board[0][global_y][global_x]["background"] = "black"
                board[0][y][x]["background"] = "blue"
                global_x = x
                global_y = y
            else:
                board[0][global_y][global_x]["background"] = "black"
                if(valid_move(x,y)):
                    if(y == 0 and board[1][y][x] == enums.Type.RED_PAWN):
                        board[1][y][x] = enums.Type.RED_KING
                    elif(y == 7 and board[1][y][x] == enums.Type.BLACK_PAWN):
                        board[1][y][x] = enums.Type.BLACK_KING
                    board[1][global_y][global_x] = 0
                global_x = -1
                global_y = -1

def create_piece(canvas, color):
    canvas.create_oval(5, 5, 75, 75, fill="white")
    canvas.create_oval(7, 7, 73, 73, fill=color)
    canvas.create_oval(10, 10, 70, 70, fill="white")
    canvas.create_oval(12, 12, 68, 68, fill=color)

for r in range(8):
    for c in range(8):
        if(((r % 2 == 0) and (c % 2 == 0)) or ((r % 2 == 1) and (c % 2 == 1))):
            board[0][r][c] = Canvas(tk, bg="red", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
        else:
            board[0][r][c] = Canvas(tk, bg="black", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
            if(r < 3):
                create_piece(board[0][r][c],"black")
                board[1][r][c] = enums.Type.BLACK_PAWN
            elif(r > 4):
                create_piece(board[0][r][c],"red")
                board[1][r][c] = enums.Type.RED_PAWN
tk.bind("<Button-1>", click)
tk.resizable(width=False, height=False)
tk.mainloop()

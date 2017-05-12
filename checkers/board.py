import enums
from  tkinter import *
from piece import Piece
tk = Tk()
board = [[[0 for x in range(8)]for y in range(8)] for z in range(2)]
global_x = -1
global_y = -1
def compress(x,y):
    global global_y
    global global_x
    board[1][y][x] = board[1][global_y][global_x]
    board[1][global_y][global_x] = 0
    create_piece(y,x)
    board[0][global_y][global_x].delete("all")
def valid_move(x, y):
    global global_y
    global global_x
    if(board[1][global_y][global_x].type): #if its a king
        print("its a king")
        if(board[1][global_y][global_x].color == "red"):
            print("its a red piece")
        else:
            print("its a black piece")
    else:
        if(abs(global_x-x) == 1 and global_y-y == (1 if board[1][global_y][global_x].color == "red" else -1)):
            compress(x,y)
        elif(abs(global_x-x) == 2 and global_y-y == (2 if board[1][global_y][global_x].color == "red" else -2)):
            if(global_x-x == -2): #if its on the right
                if(board[1][global_y][global_x].color != board[1][global_y +(-1 if board[1][global_y][global_x].color == "red" else 1)][global_x+1].color):
                    board[0][global_y + (-1 if board[1][global_y][global_x].color == "red" else 1)][global_x+1].delete("all")
                    board[1][global_y + (-1 if board[1][global_y][global_x].color == "red" else 1)][global_x+1] = 0;
                    compress(x,y)
            #else:


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
                        board[0][y][x].delete("all")
                        create_king(board[0][y][x], "red")
                    elif(y == 7 and board[1][y][x] == enums.Type.BLACK_PAWN):
                        board[1][y][x] = enums.Type.BLACK_KING
                        board[0][y][x].delete("all")
                        create_king(board[0][y][x], "black")
                    board[1][global_y][global_x] = 0
                global_x = -1
                global_y = -1
def create_piece(r,c):
    color = board[1][r][c].color
    board[0][r][c].create_oval(5, 5, 75, 75, fill="white")
    board[0][r][c].create_oval(7, 7, 73, 73, fill=color)
    board[0][r][c].create_oval(10, 10, 70, 70, fill="white")
    board[0][r][c].create_oval(12, 12, 68, 68, fill=color)
    if(board[1][r][c].type):
        canvas.create_oval(17, 17, 63, 63, fill="white")
        canvas.create_oval(19, 19, 61, 61, fill=color)

for r in range(8):
    for c in range(8):
        if(((r % 2 == 0) and (c % 2 == 0)) or ((r % 2 == 1) and (c % 2 == 1))):
            board[0][r][c] = Canvas(tk, bg="red", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
        else:
            board[0][r][c] = Canvas(tk, bg="black", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
            if(r < 3):
                board[1][r][c] = Piece(enums.Type.PAWN, enums.Type.BLACK)
                create_piece(r,c)
            elif(r > 4):
                board[1][r][c] = Piece(enums.Type.PAWN, enums.Type.RED)
                create_piece(r,c)
tk.bind("<Button-1>", click)
tk.resizable(width=False, height=False)
tk.mainloop()

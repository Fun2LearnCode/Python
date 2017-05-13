import enums
from  tkinter import *
from piece import Piece
root = Tk()
board = [[[0 for x in range(8)]for y in range(8)] for z in range(2)]
global_x = -1
global_y = -1
def compress(x,y):
    board[1][y][x] = board[1][global_y][global_x]
    board[1][global_y][global_x] = 0
    create_piece(y,x)
    board[0][global_y][global_x].delete("all")
    return True
def jump_logic(x, y, w,z):
    if(0 < global_y + y and global_y + y < 8 and 0 < global_x + x and global_x + x < 8 and board[1][global_y + y][global_x+x] !=0 and board[1][global_y][global_x].color != board[1][global_y + y][global_x+x].color):
        board[0][global_y + y][global_x+x].delete("all")
        board[1][global_y + y][global_x+x] = 0;
        return compress(w,z)
    else:
        if( 0 < global_y - y and global_y - y < 8 and 0 < global_x + x and global_x + x < 8 and board[1][global_y -y][global_x+x] !=0 and board[1][global_y][global_x].color != board[1][global_y - y][global_x+x].color):
            board[0][global_y -y][global_x+x].delete("all")
            board[1][global_y -y][global_x+x] = 0;
            return compress(w,z)

def valid_move(x, y):
    global global_y
    global global_x
    if(board[1][global_y][global_x].type): #if its a king
        if(abs(global_x-x) == 1 and abs(global_y-y) == 1):
            return compress(x,y)
        elif(abs(global_x-x) == 2 and abs(global_y-y) == 2):
            if(global_x-x == -2): #if its on the right
                return jump_logic(1,1,x,y)
            elif(global_x - x == 2):
                return jump_logic(-1,-1,x,y)
    else:
        if(abs(global_x-x) == 1 and global_y-y == (1 if board[1][global_y][global_x].color == "red" else -1)):
            return compress(x,y)
        elif(abs(global_x-x) == 2 and global_y-y == (2 if board[1][global_y][global_x].color == "red" else -2)):
            if(global_x-x == -2): #if its on the right
                return jump_logic(1,-1 if board[1][global_y][global_x].color == "red" else 1,x,y)
            else:
                return jump_logic(-1,-1 if board[1][global_y][global_x].color == "red" else 1,x,y)
def click(event):
    global global_y
    global global_x
    x = int((root.winfo_pointerx() - root.winfo_rootx())/80)
    y = int((root.winfo_pointery() - root.winfo_rooty())/80)
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
                    if(y == 0 or y== 7 and not board[1][y][x].type):
                        board[1][y][x].king_me()
                        board[0][y][x].delete("all")
                        create_piece(y,x)
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
        board[0][r][c].create_oval(17, 17, 63, 63, fill="white")
        board[0][r][c].create_oval(19, 19, 61, 61, fill=color)

for r in range(8):
    for c in range(8):
        if(((r % 2 == 0) and (c % 2 == 0)) or ((r % 2 == 1) and (c % 2 == 1))):
            board[0][r][c] = Canvas(root, bg="red", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
        else:
            board[0][r][c] = Canvas(root, bg="black", height=80, width=80, bd=0, highlightthickness=0, relief='ridge')
            board[0][r][c].grid(row = r,column = c)
            if(r < 3):
                board[1][r][c] = Piece(enums.Type.PAWN, enums.Type.BLACK)
                create_piece(r,c)
            elif(r > 4):
                board[1][r][c] = Piece(enums.Type.PAWN, enums.Type.RED)
                create_piece(r,c)
root.bind("<Button-1>", click)
root.resizable(width=False, height=False)
root.mainloop()

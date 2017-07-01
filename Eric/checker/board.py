from enums import Type
from piece import piece
global_x = -1
global_y = -1
from tkinter import *
root = Tk()

# Canvas(root, bg="red", height = 80, width = 80)
# grid(row =0, column=0)
# create_oval(5, 5, 75, 75, fill = "white")
# create_oval(10, 10, 70, 70, fill="red")
def move(x,y):
    if board[1][global_y][global_x].type:
        if board[1][global_y][global_x].color == "red" and abs(global_y - y)==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            board[0][global_y][global_x].delete("all")
            board[1][y][x] = board[1][global_y][global_x]
            board[1][global_y][global_x] = 0
            screate_piece( y,x)
        if board[1][global_y][global_x].color == "black" and abs(global_y - y)==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            board[0][global_y][global_x].delete("all")
            board[1][y][x] = board[1][global_y][global_x]
            board[1][global_y][global_x] = 0
            create_piece( y,x)
    else:
        if board[1][global_y][global_x].color == "red" and global_y - y==1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            board[0][global_y][global_x].delete("all")
            board[1][y][x] = board[1][global_y][global_x]
            board[1][global_y][global_x] = 0
            create_piece( y,x)
        elif board[1][global_y][global_x].color == "black" and global_y - y==-1 and board[1][y][x] == 0 and abs(global_x - x) == 1:
            board[0][global_y][global_x].delete("all")
            board[1][y][x] = board[1][global_y][global_x]
            board[1][global_y][global_x] = 0
            create_piece( y,x)
def jump_piece(x,y):
    if board[1][global_y][global_x].type == False:
        if board[1][global_y][global_x].color == "black" and y> global_y:
            if x<global_x and board[1][y][x] ==0 and board[1][y-1][x+1].color=="red":#black left
                board[0][global_y][global_x].delete("all")
                board[0][y-1][x+1].delete("all")
                board[1][y][x] = board[1][global_y][global_x]
                board[1][global_y][global_x] = 0
                board[1][y-1][x+1] = 0
                create_piece( y,x)
            elif x>global_x and board[1][y][x] ==0 and board[1][y-1][x-1].color=="red":#black right
                print("qwerty")
                board[0][global_y][global_x].delete("all")
                board[0][y-1][x-1].delete("all")
                board[1][y][x] = board[1][global_y][global_x]
                board[1][global_y][global_x] = 0
                board[1][y-1][x-1] = 0
                create_piece( y,x)
        elif  board[1][global_y][global_x].color == "red" and y<global_y:
            if x<global_x and board[1][y][x] ==0 and board[1][y+1][x+1].color=="black":#left
                board[0][global_y][global_x].delete("all")
                board[0][y+1][x+1].delete("all")
                board[1][y][x] = board[1][global_y][global_x]
                board[1][global_y][global_x] = 0
                board[1][y+1][x+1] = 0
                create_piece( y,x)
            elif x>global_x and board[1][y][x] ==0 and board[1][y+1][x-1].color=="black":
                board[0][global_y][global_x].delete("all")
                board[0][y+1][x-1].delete("all")
                board[1][y][x] = board[1][global_y][global_x]
                board[1][global_y][global_x] = 0
                board[1][y+1][x-1] = 0
                create_piece( y,x)
def create_piece(x, y):
    color = board[1][x][y].color
    board[0][x][y].create_oval(8, 8, 72, 72, fill = "white")
    board[0][x][y].create_oval(10, 10, 70, 70, fill=color)
    if board[1][x][y].type:
        board[0][x][y].create_oval(12, 12, 68, 68, fill = "white")
        board[0][x][y].create_oval(14, 14, 66, 66, fill=color)
def click(event):
    global global_x
    global global_y
    x= int((root.winfo_pointerx() - root.winfo_rootx())/80)
    y= int((root.winfo_pointery() - root.winfo_rooty())/80)
    if board[0][y][x]["background"] == "black":
        if global_x == -1 :
            if board[1][y][x] != 0:
                global_x = x
                global_y =y
                board[0][y][x]["background"] = "blue"
        else:
            if board[1][y][x]!= 0 :
                board[0][global_y][global_x]["background"] = "black"
                board[0][y][x]["background"] = "blue"
                global_x = x
                global_y =y
            else:
                board[0][global_y][global_x]["background"] = "black"
                if abs(global_x-x) ==1 and abs(global_y-y)==1:
                    move(x,y)
                    if y==7 or y ==0:
                        board[1][y][x].king()
                        board[1][y][x]=0
                        #create_piece( y,x)
                elif abs(global_x-x) ==2 and abs(global_y-y)==2:
                    jump_piece(x,y)
                global_x = -1
                global_y = -1
board = [[[0 for x in range(8)] for y in range(8)] for z in range(2)]
for x in range(8):
    for y in range(8):
        if x%2==0:
            if y%2==0:
                board[0][x][y]=Canvas(root, bg="red", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
            else:
                board[0][x][y]=Canvas(root, bg="black", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
                if x<=2:
                    board[1][x][y] = piece(Type.PAWN, Type.BLACK)
                    create_piece( x, y)
                elif x>=5:
                    board[1][x][y] = piece(Type.PAWN, Type.RED)
                    create_piece( x, y)
        else:
            if y%2 == 0:
                board[0][x][y]= Canvas(root, bg="black", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
                if x<=2:
                    board[1][x][y] = piece(Type.PAWN, Type.BLACK)
                    create_piece( x, y)
                elif x>=5:
                    board[1][x][y] = piece(Type.PAWN, Type.RED)
                    create_piece( x, y)
            else:
                board[0][x][y]= Canvas(root, bg="red", height = 80, width = 80, bd=0, highlightthickness =0, relief = "ridge")
                board[0][x][y].grid(row=x, column=y)
root.bind("<Button-1>", click)
root.resizable(width = False, height = False)
root.mainloop()

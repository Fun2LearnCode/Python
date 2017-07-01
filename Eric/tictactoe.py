board = [[0 for x in range(3)] for y in range(3)]


move = 0
playing = True
for x in range(3):
    for y in range(3):
        board[x][y] = "-"
def check_board():
    global playing
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] !="-":
        if board[0][0] == "x":
            print("player 1 wins")
            playing = False
        else:
            print("player2 wins")
            playing = False
    for x in range(3):
        if board[x][0] == board[x][1] == board [x][2] and board[x][1] !="-":
            if board[x][0] == "x":
                print("player 1 wins")
                playing = False
            else:
                print("player2 wins")
                playing = False
        if board[0][x] == board[1][x] == board [2][x] and board[1][x] !="-":
            if board[0][x] == "x":
                print("player 1 wins")
                playing = False
            else:
                print("player2 wins")
                playing = False
def print_board():
    for x in range(3):
        for y in range(3):
            print(board[x][y], end='')
        print("")

while playing == True:
    y = eval(input("what is the x coordinate of your move?"))
    x = eval(input("what is the y coordinate of your move?"))
    if move%2==0:
        if board[x][y] !="x" and board[x][y]!="o":
            board[x][y]="x"
            move+=1
    else:
        if board[x][y] !="x" and board[x][y] != "o":
            board[x][y]="o"
            move+=1
    print_board()
    if move>= 5:
        check_board()
    if move==9 and playing:
        print("This is a tie.")
        playing = False

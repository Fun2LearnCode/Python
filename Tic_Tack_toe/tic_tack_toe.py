board = [[0 for x in range(3)] for y in range(3)]
playing = True
moves = 0
player_one = raw_input("Enter Player one's name: ")
player_two = raw_input("Enter Player two's name: ")
for x in range(3):
    for y in range(3):
        board[x][y] = "-"

def print_board():
    for x in range(3):
        for y in range(3):
            print(board[x][y]),
        print

def check_winner():
    if board[0][0] == board[1][1] == board [2][2] and board[1][1] != "-":
        if board[0][0] == "x":
            print(player_one +" Wins!")
        else:
            print(player_two + " Wins!")
        return True
    for x in range(3):
        if board[0][x] == board[1][x] == board [2][x] and board[1][x] != "-":
            if board[0][x] == "x":
                print(player_one +" Wins!")
            else:
                print(player_two + " Wins!")
            return True
        if board[x][0] == board[x][1] == board [x][2] and board[x][1] != "-":
            if board[x][0] == "x":
                print(player_one + " Wins!")
            else:
                print(player_two + " Wins!")
            return True
    return False
    
while playing:
    if moves % 2 == 0:
        print(player_one + "\'s turn")
    else:
        print(player_two + "\'s turn")
    ycord = input("input x coordinate: ") - 1
    xcord = input("input y coordinate: ") -1
    if board[xcord][ycord] == "-":
        if moves % 2 == 0:
            board[xcord][ycord] = 'x'
        else:
            board[xcord][ycord] = 'o'
        moves += 1
        print_board()
    if moves > 2:
        if check_winner():
            playing = False
    if moves == 9:
        playing = False
if check_winner() == False:
    print("It's a Draw!")
print_board()

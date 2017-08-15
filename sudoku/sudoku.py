from  tkinter import *
root = Tk()
sudoku_board = [[0 for x in range(3)]for y in range(3)]
menu_bar = Menu(root)
game = Menu(root, tearoff=0)
difficulty = Menu(root, tearoff=0)

def reset_puzzle():
    print()
def new_puzzle():
    print()
def check_puzzle():
    print()
def load_puzzle(level):
    print()
difficulty.add_command(label="Beginner", command=load_puzzle(0))
difficulty.add_command(label="intermediate", command=load_puzzle(1))
difficulty.add_command(label="Advanced", command=load_puzzle(2))
difficulty.add_command(label="Impossible?", command=load_puzzle(3))
game.add_command(label="reset", command=reset_puzzle)
game.add_command(label="new puzzle", command=new_puzzle)
game.add_command(label="check", command=check_puzzle)
menu_bar.add_cascade(label="game", menu=game)
menu_bar.add_cascade(label="difficulty", menu=difficulty)
root.config(menu = menu_bar)
root.resizable(width=False, height=False)
root.mainloop()

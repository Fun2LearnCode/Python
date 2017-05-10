import Enums
class Piece:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
    def king_me(self):
        if(self.type == 3):
            self.type = Enums.Type.BLACK_KING
        else:
            self.type = Enums.Type.RED_KING
    def move(self, direction):
        if(direction == Enums.Move.UP_LEFT):
            self.x -= 1
            self.y -= 1
        elif(direction == Enums.Move.UP_RIGHT):
            self.x += 1
            self.y -= 1
        elif(direction == Enums.Move.DOWN_LEFT):
            self.x -= 1
            self.y += 1
        elif(direction == Enums.Move.DOWN_RIGHT):
            self.x += 1
            self.y += 1
        elif(direction == Enums.Move.JUMP_UP_LEFT):
            self.x -= 2
            self.y -= 2
        elif(direction == Enums.Move.JUMP_UP_RIGHT):
            self.x += 2
            self.y -= 2
        elif(direction == Enums.Move.JUMP_DOWN_LEFT):
            self.x -= 2
            self.y += 2
        else:
            self.x += 2
            self.y += 2

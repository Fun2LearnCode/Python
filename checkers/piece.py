from enums import Type
class Piece:
    def __init__(self, type, color):
        self.color = color
        self.type = type
    def king_me(self):
        self.type = Type.KING

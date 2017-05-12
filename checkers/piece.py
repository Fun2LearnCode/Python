import enums
class Piece:
    def __init__(self, type, color):
        self.color = color
        self.type = type
    def king_me(self):
        self.type = enums.Type.KING

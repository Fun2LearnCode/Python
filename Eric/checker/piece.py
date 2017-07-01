from enums import Type
class piece:
    def __init__(self, type, color):
        self.color = color
        self.type = type
    def king(self):
        self.type = Type.KING

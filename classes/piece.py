from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, x, y, color, type):
        self.x = x
        self.y = y
        self.color = color
        self.type = type

    @abstractmethod
    def get_valid_moves(self, board):
        return []
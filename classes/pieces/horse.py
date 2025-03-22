import math
from classes.piece import Piece

class Horse(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Horse')
    
    def get_valid_moves(self, board):
        moves = []
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < 10 and 0 <= new_y < 9:
                if board.grid[new_x][new_y] is None or board.grid[new_x][new_y].color != self.color:
                    if board.grid[self.x + math.trunc(dx / 2)][self.y + math.trunc(dy / 2)] is None:
                        moves.append((new_x, new_y))
        return moves
from classes.piece import Piece

class Soldier(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Soldier')

    def get_valid_moves(self, board):
        moves = []
        directions = {'r': [(-1, 0)], 'b': [(1, 0)]}
        if (self.color == 'r' and 9 - self.x >= 5) or (self.color == 'b' and self.x >= 5):
            directions = {
            'r': [(-1, 0), (0,-1), (0, 1)],
            'b': [(1, 0), (0,-1), (0, 1)]
            }
        for dx, dy in directions[self.color]:
            new_x, new_y  = self.x + dx, self.y + dy
            if 0 <= new_x < 10 and 0 <= new_y < 9:
                if board.grid[new_x][new_y] is None or board.grid[new_x][new_y].color != self.color:
                    moves.append((new_x, new_y))
        return moves
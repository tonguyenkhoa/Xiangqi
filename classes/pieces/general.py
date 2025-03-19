from classes.piece import Piece

class General(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'General')

    def get_valid_moves(self, board):
        moves = []
        limit_range = {
            'b': [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
            'r': [(9, 3), (9, 4), (9, 5), (8, 3), (8, 4), (8, 5), (7, 3), (7, 4), (7, 5)]
        }
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            # general is not allowed to leave the capital
            if (new_x, new_y) in limit_range[self.color]:
                if board.grid[new_x][new_y] is None or board.grid[new_x][new_y].color != self.color:
                    moves.append((new_x, new_y))
        return moves


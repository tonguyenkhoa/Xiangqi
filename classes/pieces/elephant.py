from classes.piece import Piece

class Elephant(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Elephant')

    def get_valid_moves(self, board):
        moves = []
        directions = [(2, 2), (-2, -2), (2, -2), (-2, 2)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            if self.color == 'r':
                distance = 9 - new_x
            else:
                distance = new_x
            # distance <= 4 means the elephant have not yet crossed the river    
            if 0 <= new_x < 10 and 0 <= new_y < 9 and distance <= 4:
                if board.grid[new_x][new_y] is None or board.grid[new_x][new_y].color != self.color:
                    if board.grid[self.x + (dx // 2)][self.y + (dy // 2)] is None:
                        moves.append((new_x, new_y))
        return moves
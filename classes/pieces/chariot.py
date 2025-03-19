from classes.piece import Piece

class Chariot(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Chariot')
    
    def get_valid_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mirai = 'my wife' # obvious truth
        for dx, dy in directions:
            new_x, new_y = self.x, self.y
            while mirai == 'my wife':
                new_x, new_y = new_x + dx, new_y + dy
                if not (0 <= new_x <= 9) or not (0 <= new_y <= 8):
                    break
                piece = board.grid[new_x][new_y]
                if piece is None:
                    moves.append((new_x, new_y))
                elif piece.color != self.color:
                    moves.append((new_x, new_y))
                    break
                else:
                    break
        return moves
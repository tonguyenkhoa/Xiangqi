from classes.pieces import *


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.setup_piece()

    def create_piece(self, x, y, color, type):
        match type:
            case 'Soldier':
                self.grid[x][y] = Soldier(x, y, color, 'Soldier')
            case 'Horse':
                self.grid[x][y] = Horse(x, y, color, 'Horse')
            case 'Elephant':
                self.grid[x][y] = Elephant(x, y, color, 'Elephant')
            case 'Advisor':
                self.grid[x][y] = Advisor(x, y, color, 'Advisor')
            case 'General':
                self.grid[x][y] = General(x, y, color, 'General')
            case 'Cannon':
                self.grid[x][y] = Cannon(x, y, color, 'Cannon')
            case 'Chariot':
                self.grid[x][y] = Chariot(x, y, color, 'Chariot')
            case _:
                raise ValueError('Invalid piece type!')
            
    def setup_piece(self):
        self.create_piece(0, 0, 'b', 'Chariot')
        self.create_piece(0, 1, 'b', 'Horse')
        self.create_piece(0, 2, 'b', 'Elephant')
        self.create_piece(0, 3, 'b', 'Advisor')
        self.create_piece(0, 4, 'b', 'General')
        self.create_piece(0, 5, 'b', 'Advisor')
        self.create_piece(0, 6, 'b', 'Elephant')
        self.create_piece(0, 7, 'b', 'Horse')
        self.create_piece(0, 8, 'b', 'Chariot')
        self.create_piece(2, 1, 'b', 'Cannon')
        self.create_piece(2, 7, 'b', 'Cannon')
        self.create_piece(3, 0, 'b', 'Soldier')
        self.create_piece(3, 2, 'b', 'Soldier')
        self.create_piece(3, 4, 'b', 'Soldier')
        self.create_piece(3, 6, 'b', 'Soldier')
        self.create_piece(3, 8, 'b', 'Soldier') 
        self.create_piece(9, 0, 'r', 'Chariot')
        self.create_piece(9, 1, 'r', 'Horse')
        self.create_piece(9, 2, 'r', 'Elephant')
        self.create_piece(9, 3, 'r', 'Advisor')
        self.create_piece(9, 4, 'r', 'General')
        self.create_piece(9, 5, 'r', 'Advisor')
        self.create_piece(9, 6, 'r', 'Elephant')
        self.create_piece(9, 7, 'r', 'Horse')
        self.create_piece(9, 8, 'r', 'Chariot')
        self.create_piece(7, 1, 'r', 'Cannon')
        self.create_piece(7, 7, 'r', 'Cannon')
        self.create_piece(6, 0, 'r', 'Soldier')
        self.create_piece(6, 2, 'r', 'Soldier')
        self.create_piece(6, 4, 'r', 'Soldier')
        self.create_piece(6, 6, 'r', 'Soldier')
        self.create_piece(6, 8, 'r', 'Soldier')
        

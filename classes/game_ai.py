import math
import tkinter as tk
import pygame
from PIL import Image, ImageTk
from tkinter import messagebox
from classes.ai import AI

cell_size = 80
piece_size = 60
earthy_orange = '#D0882C'
dark_brown = '#803300'
lemon_chiffon = '#FFFACD'
WIDTH = 740
HEIGHT = 820
river_words = ['楚', '河', '漢', '界']
engine_path = '/home/mihari/CODE/Python/Xiangqi/pikafish_ai/Pikafish/src/pikafish'

class Game_AI:
    def __init__(self, root, board):        
        # Initialize the interface
        self.root = root
        self.root.title('Xiangqi')
        self.board = board

        # Get screen's size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the position so that the window is in the middle of the screen
        x_position = (screen_width - WIDTH) // 2
        y_position = (screen_height - HEIGHT) // 2

        # Set window's position
        root.geometry(f'{WIDTH}x{HEIGHT}+{x_position}+{y_position}')

        self.board = board
        self.selected_piece = None
        self.ai = AI(engine_path)
        self.turn = 'r'

        # Create sound's effect
        pygame.mixer.init()
        self.move_check_sound = pygame.mixer.Sound('assets/audio/move_check.mp3')
        self.move_self_sound = pygame.mixer.Sound('assets/audio/move_self.mp3')
        self.start_sound = pygame.mixer.Sound('assets/audio/start.mp3')
        self.end_sound = pygame.mixer.Sound('assets/audio/end.mp3')
        self.another_end_sound = pygame.mixer.Sound('assets/audio/another_end.mp3') 

        # Create a canvas to draw board
        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg = dark_brown)
        self.canvas.pack()

        # Load images
        self.piece_images = self.load_piece_images()

        # Catch mouse's click event
        self.canvas.bind('<Button-1>', self.on_click)

        # Draw
        self.draw_board()

        # Play the start sound
        self.start_sound.play()

    def draw_board(self):
        self.canvas.delete('all')
        self.draw_grid()
        self.draw_pieces()

    def draw_cross_marks(self, x, y):
        col = 50 + x * cell_size
        row = 50 + y * cell_size
        dis = 7
        if y == 0:
            self.canvas.create_line(row + dis, col - dis * 2, row + dis, col - dis, width = 2)
            self.canvas.create_line(row + dis, col - dis, row + dis * 2, col - dis, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis, col + dis * 2, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis * 2, col + dis, width = 2)
        elif y == 8:
            self.canvas.create_line(row - dis, col - dis * 2, row - dis, col - dis, width = 2)
            self.canvas.create_line(row - dis, col - dis, row - dis * 2, col - dis, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis, col + dis * 2, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis * 2, col + dis, width = 2)
        else:
            self.canvas.create_line(row - dis, col - dis * 2, row - dis, col - dis, width = 2)
            self.canvas.create_line(row - dis, col - dis, row - dis * 2, col - dis, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis, col + dis * 2, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis * 2, col + dis, width = 2)
            self.canvas.create_line(row + dis, col - dis * 2, row + dis, col - dis, width = 2)
            self.canvas.create_line(row + dis, col - dis, row + dis * 2, col - dis, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis, col + dis * 2, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis * 2, col + dis, width = 2)

    def draw_grid(self):
        self.canvas.create_rectangle(50, 50, WIDTH - 50, HEIGHT - 50, fill = earthy_orange)
        for i in range(10):
            self.canvas.create_line(50, 50 + cell_size * i, WIDTH - 50, 50 + cell_size * i, width = 2)
        for j in range(9):
            if j == 0 or j == 8:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, HEIGHT - 50, width = 2)
            else:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, HEIGHT - 50 - 5 * cell_size, width = 2)
                self.canvas.create_line(50 + cell_size * j, HEIGHT - 50 - 4 * cell_size, 50 + cell_size * j, HEIGHT - 50, width = 2)
        self.canvas.create_line(WIDTH - 50 - 5 * cell_size, 50, WIDTH - 50 - 3 * cell_size, HEIGHT - 50 - 7 * cell_size, width = 2)
        self.canvas.create_line(WIDTH - 50 - 3 * cell_size, 50, WIDTH - 50 - 5 * cell_size, HEIGHT - 50 - 7 * cell_size, width = 2)
        self.canvas.create_line(WIDTH - 50 - 5 * cell_size, HEIGHT - 50 - 2 * cell_size, WIDTH - 50 - 3 * cell_size, HEIGHT - 50, width = 2)
        self.canvas.create_line(WIDTH - 50 - 3 * cell_size, HEIGHT - 50 - 2 * cell_size, WIDTH - 50 - 5 * cell_size, HEIGHT - 50, width = 2)

        self.draw_cross_marks(2, 1)
        self.draw_cross_marks(2, 7)
        self.draw_cross_marks(3, 0)
        self.draw_cross_marks(3, 2)
        self.draw_cross_marks(3, 4)
        self.draw_cross_marks(3, 6)
        self.draw_cross_marks(3, 8)
        self.draw_cross_marks(7, 1)
        self.draw_cross_marks(7, 7)
        self.draw_cross_marks(6, 0)
        self.draw_cross_marks(6, 2)
        self.draw_cross_marks(6, 4)
        self.draw_cross_marks(6, 6)
        self.draw_cross_marks(6, 8)
        
        self.canvas.create_text(50 + cell_size + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[0],
                                font = ('Arial', 50), fill = 'black')   
        self.canvas.create_text(50 + cell_size * 2 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[1],
                                font = ('Arial', 50), fill = 'black')
        self.canvas.create_text(50 + cell_size * 5 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[2],
                                font = ('Arial', 50), fill = 'black')
        self.canvas.create_text(50 + cell_size * 6 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[3],
                                font = ('Arial', 50), fill = 'black')
        
    def load_piece_images(self):
        types = [
            'Soldier', 'Horse', 'Elephant', 'Advisor', 'General', 'Cannon', 'Chariot'
        ]
        colors = ['r', 'b']
        images = {}
        for color in colors:
            for type in types:
                path = f'assets/pictures/{color}_{type}.png'
                try:
                    img = Image.open(path).resize((piece_size, piece_size))
                    images[f'{color}_{type}'] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f'Error when loading image {path}: {e}')
        return images
    
    def draw_pieces(self):
        for i in range(10):
            for j in range(9):
                piece = self.board.grid[i][j]
                if piece:
                    key = f'{piece.color}_{piece.type}'
                    if key in self.piece_images:
                        self.canvas.create_image(50 + j * cell_size, 50 + i * cell_size, 
                                                 image = self.piece_images[key], anchor = 'center')
                        
    def draw_oval(self, valid_moves):
        for move in valid_moves:
            a, b = move
            self.canvas.create_oval(40 + b * cell_size, 40 + a * cell_size, 60 + b * cell_size, 
                                                    60 + a * cell_size, fill = lemon_chiffon)
                        
    def on_click(self, event):
        # event.x,y are click's position
        col = math.floor((event.x - 50 + cell_size // 2) / cell_size)
        row = math.floor((event.y - 50 + cell_size // 2) / cell_size)
        if 0 <= row < 10 and 0 <= col < 9:
            piece = self.board.grid[row][col]
            if self.selected_piece:
                if self.is_valid_move(self.selected_piece, row, col):
                    self.complete_move(self.selected_piece, row, col)
                    if self.is_checkmated():
                        self.another_end_sound.play()
                        messagebox.showinfo('Result', f'You lose!')
                        self.root.quit()
                else:
                    if piece and piece.color == self.selected_piece.color:
                        self.selected_piece = piece
                        self.draw_board()
                        self.draw_oval(self.get_prime_valid_moves(piece))
            else:
                if piece and piece.color == self.turn:
                        self.selected_piece = piece
                        self.draw_oval(self.get_prime_valid_moves(piece))

    def get_prime_valid_moves(self, piece):
        tmp_valid_moves = []
        for current_move in piece.get_valid_moves(self.board):
            x, y = current_move
            if not self.will_general_be_irradiated_after_transfer(piece, x, y):
                tmp_valid_moves.append(current_move)
        return tmp_valid_moves

    def is_valid_move(self, piece, row, col):
        if (row, col) in piece.get_valid_moves(self.board):
            if self.will_general_be_irradiated_after_transfer(piece, row, col):
                messagebox.showinfo('Warning', 'The general will be irradiated after transfer!')
                return False
            return True
        return False

    def complete_move(self, piece, row, col):
        # Move the piece
        self.move_piece(piece, row, col) 

        print(self.grid_to_fen(self.board.grid))

        self.draw_board()
        self.window = tk.Tk()
        self.window.update()
        self.window.destroy()

        # Check if the game is over
        self.is_the_game_over(row, col)

        # AI's turn
        fen = self.grid_to_fen(self.board.grid)
        best_move = self.ai.get_ai_move(fen)
        f_row, f_col, t_row, t_col = self.fen_to_grid(best_move)
        self.move_piece(self.board.grid[f_row][f_col], t_row, t_col)
        
        self.draw_board()

    def move_piece(self, piece, row, col):
        sound = 0 if self.board.grid[row][col] else 1
        self.board.grid[piece.x][piece.y] = None  
        piece.x, piece.y = row, col  
        self.board.grid[row][col] = piece  
        self.selected_piece = None
        if sound == 0:
            self.move_check_sound.play()
        else:
            self.move_self_sound.play()

    def is_the_game_over(self, row, col):
        if self.board.grid[row][col] and self.board.grid[row][col].type == 'General':  
            self.end_sound.play()
            messagebox.showinfo('Result', f'Red is the winner!')
            self.root.quit()
    
    def will_general_be_irradiated_after_transfer(self, piece, new_x, new_y):
        old_x, old_y = piece.x, piece.y
        captured_piece = self.board.grid[new_x][new_y]

        self.board.grid[old_x][old_y] = None
        self.board.grid[new_x][new_y] = piece
        piece.x, piece.y = new_x, new_y

        check = self.is_general_in_check(piece.color) or self.is_general_face_to_face()

        self.board.grid[old_x][old_y] = piece
        self.board.grid[new_x][new_y] = captured_piece
        piece.x, piece.y = old_x, old_y

        return check

    def is_general_in_check(self, color):
        # Find the general's position
        general_pos = self.find_general(color)
        
        # Browse all enemy's pieces
        for i in range(10):
            for j in range(9):
                piece = self.board.grid[i][j]
                if piece and piece.color != color:
                    if general_pos in piece.get_valid_moves(self.board):
                        return True
        return False
    
    def is_general_face_to_face(self):
        r_x, r_y = self.find_general('r')
        b_x, b_y = self.find_general('b')
        if r_y != b_y:
            return False
        for i in range(b_x + 1, r_x):
            if self.board.grid[i][r_y]:
                return False
        return True
    
    def find_general(self, color):
        a, b, c, d = (0, 3, 3, 6) if color == 'b' else (7, 10, 3, 6)
        for i in range(a, b):
            for j in range(c, d):
                piece = self.board.grid[i][j]
                if piece and piece.type == 'General':
                    return (i, j)

    def is_checkmated(self):
        for i in range(10):
            for j in range(9):
                piece = self.board.grid[i][j]
                if piece and piece.color == self.turn:
                    for (row, col) in piece.get_valid_moves(self.board):
                        if not self.will_general_be_irradiated_after_transfer(piece, row, col):
                            return False
        return True
    
    def grid_to_fen(self, grid):
        fen_parts = []
        for i in range(10):
            row_fen = ''
            cnt = 0
            for j in range(9):
                if grid[i][j] is None:
                    cnt += 1
                else:
                    if cnt > 0:
                        row_fen += str(cnt)
                        cnt = 0
                    row_fen += self.piece_to_fen(grid[i][j].color, grid[i][j].type)
            if cnt > 0:
                row_fen += str(cnt)
            fen_parts.append(row_fen)
        return '/'.join(fen_parts) + ' b'

    def piece_to_fen(self, color, type):
        match (color, type):
            case ('r', 'General'): return 'K'
            case ('r', 'Advisor'): return 'A'
            case ('r', 'Elephant'): return 'B'
            case ('r', 'Horse'): return 'N'
            case ('r', 'Chariot'): return 'R'
            case ('r', 'Cannon'): return 'C'
            case ('r', 'Soldier'): return 'P'
            case ('b', 'General'): return 'k'
            case ('b', 'Advisor'): return 'a'
            case ('b', 'Elephant'): return 'b'
            case ('b', 'Horse'): return 'n'
            case ('b', 'Chariot'): return 'r'
            case ('b', 'Cannon'): return 'c'
            case ('b', 'Soldier'): return 'p'
            case _: return ''
        
    def fen_to_grid(self, move):
        f_col = ord(move[0]) - ord('a')
        f_row = 9 - int(move[1])
        t_col = ord(move[2]) - ord('a')
        t_row = 9 - int(move[3])
        return f_row, f_col, t_row, t_col
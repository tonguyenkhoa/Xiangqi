import tkinter as tk
from PIL import Image, ImageTk
from classes.game_human import Game_Human
from classes.game_ai import Game_AI

WIDTH = 1200
HEIGHT = 628

class Menu:
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

        # Load background image
        self.bg_image = Image.open('assets/pictures/menu.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Set background image
        self.bg_label = tk.Label(root, image = self.bg_photo)
        self.bg_label.place(relwidth = 1, relheight = 1)
        
        # Set Label
        tk.Label(root, text = 'SELECT GAME MODE', font = ('Arial', 40)).pack(pady = 80)

        # Set Button
        tk.Button(root, text = 'Play with human', command = self.play_with_human, font = ('Arial', 30)).pack(pady = 30)
        tk.Button(root, text = 'Play with Pikafish', command = self.play_with_ai, font = ('Arial', 30)).pack(pady = 30)

    def play_with_human(self):
        self.root.destroy()  # Close menu
        root = tk.Tk()  # Create a new window for the board
        Game_Human(root, self.board)  # Open human mode

    def play_with_ai(self):
        self.root.destroy()  # Close menu
        root = tk.Tk()  # Create a new window for the board
        Game_AI(root, self.board)  # Open AI mode
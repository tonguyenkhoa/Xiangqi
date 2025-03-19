from tkinter import Tk
from classes.board import Board
from classes.game import Game

if __name__ == '__main__':
    root = Tk()
    board = Board()
    game = Game(root, board)
    root.mainloop()
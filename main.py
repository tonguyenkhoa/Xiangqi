from tkinter import Tk
from classes.board import Board
from classes.menu import Menu

if __name__ == '__main__':
    root = Tk()
    board = Board()
    menu = Menu(root, board)
    root.mainloop()
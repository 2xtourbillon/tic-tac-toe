import tkinter as tk

# main ttt class
class TICTACTOE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.btns = []
        self.turn = True
        self.count = 0 #check if any turns are left
        self.resizable(width=False, height=False) #disable resize window button
        self.Board() #create the game board



TICTACTOE().mainloop()
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

    def Board(self):
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(tk.Button(self, width=10, height=3, font='Calibri 35 bold',
                            command=lambda x=1, y=j: self.Turn_Taken(x, y)))
                row[j].grid(row=i, column=j)
            self.btns.append(row) #appending row to entire window
        tk.Button(self, text='New Game', width=10, height=1, font='Calibri 15 bold',
                  bg='black', fg='white', activebackground='blue3', activeforeground='white',
                  command=self.NEWGAME).grid(row=3, column=1)

    def Turn_Taken(self, x, y):
        self.count += 1
        
        # taking your turn; 'X' will go always first
        if self.turn:
            char = 'X'
            self.btns[x][y].config(text='X', bg='black', state='disabled')
        else:
            char = 'O'
            self.btns[x][y].config(text='O', bg='white', state='disabled')
        
        # checking the results of after turn
        self.Check_Results(char)

        # give turn to second player
        self.turn = not self.turn


TICTACTOE().mainloop()
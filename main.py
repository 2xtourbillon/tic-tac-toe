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
                            command=lambda x=i, y=j: self.Turn_Taken(x, y)))
                row[j].grid(row=i, column=j)
            self.btns.append(row) #appending row to entire window
        tk.Button(self, text='New Game', width=10, height=1, font='Calibri 15 bold',
                  bg='black', fg='white', activebackground='blue3', activeforeground='white',
                  command=self.NEWGAME).grid(row=3, column=1)

    # taking a turn
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

    # destroy and create new game
    def NEWGAME(self):
        for widget in self.winfo_children():
            widget.destroy()
        # resetting vars
        self.btns = []
        self.turn = True
        self.count = 0
        # build the board
        self.Board()

    # checking the results
    def Check_Results(self, char):
        # check the rows
        if ((
            (self.btns[0][0]['text'] == char) and 
            (self.btns[0][1]['text'] == char) and
            (self.btns[0][2]['text'] == char)
        ) 
        or (
            (self.btns[1][0]['text'] == char) and
            (self.btns[1][1]['text'] == char) and
            (self.btns[1][2]['text'] == char)
        )
        or (
            (self.btns[2][0]['text'] == char) and
            (self.btns[3][1]['text'] == char) and
            (self.btns[4][2]['text'] == char)
            )):
                pass
        # check the columns
        elif ((
            (self.btns[0][0]['text'] == char) and 
            (self.btns[1][0]['text'] == char) and
            (self.btns[2][0]['text'] == char)
        ) 
        or (
            (self.btns[0][1]['text'] == char) and
            (self.btns[1][1]['text'] == char) and
            (self.btns[2][1]['text'] == char)
        )
        or (
            (self.btns[0][2]['text'] == char) and
            (self.btns[1][2]['text'] == char) and
            (self.btns[2][2]['text'] == char)
        )):
            pass
        
        # diagonal conditions
        elif ((
            (self.btns[0][0]['text'] == char) and 
            (self.btns[1][1]['text'] == char) and
            (self.btns[2][2]['text'] == char)
        ) 
        or (
            (self.btns[0][2]['text'] == char) and
            (self.btns[1][1]['text'] == char) and
            (self.btns[2][0]['text'] == char)
        )):
            pass
        



TICTACTOE().mainloop()
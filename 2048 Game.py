import tkinter as tk
import random
import time

class Game(tk.Tk):
    board = []
    new_tile_selection = [2,2,2,2,2,2,4]
    score = 0
    highscore = 0
    scorestring = 0
    highscorestring = 0
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.scorestring = tk.StringVar(self)
        self.scorestring.set("0")
        self.highscorestring = tk.StringVar(self)
        self.highscorestring.set("0")
        self.create_widgets()
        self.canvas = tk.Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="false")
        self.new_game()

    #Adds 1 new tiles to board in empty spaces, highlights tile
    def addNewTile(self):
        index = random.randint(0,6)
        x = -1
        y = -1
        while self.isFull() == False:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if (self.board[x][y] == 0):
                self.board[x][y] = self.new_tile_selection[index]
                x1 = y*105
                y1 = x*105
                x2 = x1 + 105 - 5
                y2 = y1 + 105 - 5
                num = self.board[x][y]
                if num == 2:
                    self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="", width=0)
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#f78a8a", text="2")
                elif num == 4:
                    self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b8dbe5", tags="rect",  outline="", width=0)
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#f78a8a", text="4")
            
                
                break
    #Returns True if board is full
    def isFull(self):
        for i in range(0,4):
            for j in range(0,4):
                if (self.board[i][j] == 0):
                    return False
        return True
    #Prints game board
    def printboard(self):
        cellwidth = 105
        cellheight = 105
        self.square = {}

        for column in range(4):
            for row in range(4):
                x1 = column*cellwidth
                y1 = row*cellheight
                x2 = x1 + cellwidth - 5
                y2 = y1 + cellheight - 5
                num = self.board[row][column]
                if num == 0:
                    self.print0(row, column, x1, y1, x2, y2)
                elif num == 2:
                    self.print2(row, column, x1, y1, x2, y2)
                elif num == 4:
                    self.print4(row, column, x1, y1, x2, y2)
                elif num == 8:
                    self.print8(row, column, x1, y1, x2, y2)
                elif num == 16:
                    self.print16(row, column, x1, y1, x2, y2)
                elif num == 32:
                    self.print32(row, column, x1, y1, x2, y2)
                elif num == 64:
                    self.print64(row, column, x1, y1, x2, y2)
                elif num == 128:
                    self.print128(row, column, x1, y1, x2, y2)
                elif num == 256:
                    self.print256(row, column, x1, y1, x2, y2)
                elif num == 512:
                    self.print512(row, column, x1, y1, x2, y2)
                elif num == 1024:
                    self.print1024(row, column, x1, y1, x2, y2)
                elif num == 2048:
                    self.print2048(row, column, x1, y1, x2, y2) 

    def print0(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#f5f5f5", tags="rect", outline="")
    def print2(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#494949", text="2")
    def print4(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b8dbe5", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#494949", text="4")
    def print8(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#71b1bd", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="8")
    def print16(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#27819f", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="16")
    def print32(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#0073b9", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="32")
    def print64(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#7fa8d7", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="64")
    def print128(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#615ea6", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="128")
    def print256(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#2f3490", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="256")
    def print512(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#1c1862", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="512")
    def print1024(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#9c005d", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="1024")
    def print2048(self, row, column, x1, y1, x2, y2):
        self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#c80048", tags="rect", outline="")
        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="2048")

    #Creates buttons at top of screen
    def create_widgets(self):
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=2, column=0, columnspan=4)
        tk.Button(self.buttonframe, text = "New Game",command=self.new_game).grid(row=0, column=0)
        tk.Label(self.buttonframe, text = "Score:").grid(row=0, column=1)
        tk.Label(self.buttonframe, textvariable=self.scorestring).grid(row=0, column=2)
        tk.Label(self.buttonframe, text = "Record:").grid(row=0, column=3)
        tk.Label(self.buttonframe, textvariable=self.highscorestring).grid(row=0, column=4)        
        self.buttonframe.pack(side="top")

    #executes moves based on arroy keys pressed
    def keyPressed(self,event):
        shift = 0
        if event.keysym == 'Down':
            for j in range(0,4):
                shift = 0
                for i in range(3,-1,-1):
                    if self.board[i][j] == 0:
                        shift += 1
                    else:
                        if i - 1 >= 0 and self.board[i-1][j] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i-1][j] = 0
                        elif i - 2 >= 0 and self.board[i-1][j] == 0 and self.board[i-2][j] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i-2][j] = 0
                        elif i == 3 and self.board[2][j] + self.board[1][j] == 0 and self.board[0][j] == self.board[3][j]:
                            self.board[3][j] *= 2
                            self.score += self.board[3][j]
                            self.board[0][j] = 0
                        if shift > 0:
                            self.board[i+shift][j] = self.board[i][j]
                            self.board[i][j] = 0
            self.printboard()
            self.addNewTile() 
            self.isOver()
        elif event.keysym == 'Right':
            for i in range(0,4):
                shift = 0
                for j in range(3,-1,-1):
                    if self.board[i][j] == 0:
                        shift += 1
                    else:
                        if j - 1 >= 0 and self.board[i][j-1] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i][j-1] = 0
                        elif j - 2 >= 0 and self.board[i][j-1] == 0 and self.board[i][j-2] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i][j-2] = 0
                        elif j == 3 and self.board[i][2] + self.board[i][1] == 0 and self.board[0][j] == self.board[3][j]:
                            self.board[i][3] *= 2
                            self.score += self.board[i][3]
                            self.board[i][0] = 0
                        if shift > 0:
                            self.board[i][j+shift] = self.board[i][j]
                            self.board[i][j] = 0
            self.printboard()
            self.addNewTile() 
            self.isOver()
        elif event.keysym == 'Left':
            for i in range(0,4):
                shift = 0
                for j in range(0,4):
                    if self.board[i][j] == 0:
                        shift += 1
                    else:
                        if j + 1 < 4 and self.board[i][j+1] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i][j+1] = 0
                        elif j + 2 < 4 and self.board[i][j+1] == 0 and self.board[i][j+2] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i][j+2] = 0
                        elif j == 0 and self.board[i][1] + self.board[i][2] == 0 and self.board[i][3] == self.board[i][0]:
                            self.board[i][0] *= 2
                            self.score += self.board[i][0]
                            self.board[i][3] = 0
                        if shift > 0:
                            self.board[i][j-shift] = self.board[i][j]
                            self.board[i][j] = 0
            self.printboard()
            self.addNewTile() 
            self.isOver()
        elif event.keysym == 'Up':
            for j in range(0,4):
                shift = 0
                for i in range(0,4):
                    if self.board[i][j] == 0:
                        shift += 1
                    else:
                        if i + 1 < 4 and self.board[i+1][j] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i+1][j] = 0
                        elif i + 2 < 4 and self.board[i+1][j] == 0 and self.board[i+2][j] == self.board[i][j]:
                            self.board[i][j] *= 2
                            self.score += self.board[i][j]
                            self.board[i+2][j] = 0
                        elif i == 0 and self.board[1][j] + self.board[2][j] == 0 and self.board[3][j] == self.board[0][j]:
                            self.board[0][j] *= 2
                            self.score += self.board[0][j]
                            self.board[3][j] = 0
                        if shift > 0:
                            self.board[i-shift][j] = self.board[i][j]
                            self.board[i][j] = 0
            self.printboard()
            self.addNewTile() 
            self.isOver()
        self.scorestring.set(str(self.score))
        if self.score > self.highscore:
            self.highscore = self.score
            self.highscorestring.set(str(self.highscore))
        
        
    def new_game(self):
        self.score = 0
        self.scorestring.set("0")
        self.board = []
        self.board.append([0,0,0,0])
        self.board.append([0,0,0,0])
        self.board.append([0,0,0,0])
        self.board.append([0,0,0,0])
        while True:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if (self.board[x][y] == 0):
                self.board[x][y] = 2
                break

        index = random.randint(0,6)
        while self.isFull() == False:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if (self.board[x][y] == 0):
                self.board[x][y] = self.new_tile_selection[index]
                break
        self.printboard()

        
    #Returns True if board is full & has no more moves
    def isOver(self):
        for i in range(0,4):
            for j in range(0,4):
                if (self.board[i][j] == 2048):
                    self.youWon()
        for i in range(0,4):
            for j in range(0,4):
                if (self.board[i][j] == 0):
                    return False
        for i in range(0,4):
            for j in range(0,3):
                if (self.board[i][j] == self.board[i][j+1]):
                    return False
        for j in range(0,4):
            for i in range(0,3):
                if self.board[i][j] == self.board[i+1][j]:
                    return False
        gameover = [["G", "A", "M", "E",],["O", "V", "E", "R"], ["", "", "", ""],  ["", "", "", ""]]
        cellwidth = 105
        cellheight = 105
        self.square = {}

        for column in range(4):
            for row in range(4):
                x1 = column*cellwidth
                y1 = row*cellheight
                x2 = x1 + cellwidth - 5
                y2 = y1 + cellheight - 5
                self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
                self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#494949", text=gameover[row][column])
        return True
    def youWon(self):
        gameover = [["Y", "O", "U", "",],["W", "O", "N", "!"], ["", "", "", ""],  ["", "", "", ""]]
        cellwidth = 105
        cellheight = 105
        self.square = {}
        for column in range(4):
            for row in range(4):
                x1 = column*cellwidth
                y1 = row*cellheight
                x2 = x1 + cellwidth - 5
                y2 = y1 + cellheight - 5
                self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
                self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#494949", text=gameover[row][column])
        

if __name__ == "__main__":
    app = Game()
    app.bind_all('<Key>', app.keyPressed)
    app.wm_title("2048")
    app.minsize(420,450)
    app.maxsize(420,450)
    app.mainloop()






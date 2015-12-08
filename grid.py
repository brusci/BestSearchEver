import tkinter as tk
from random import randint
import game
import game_sample_run

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="white", color2="white"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        
        self.se = SearchEngine('astar', 'full')
        self.ideal_moves = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)
        #this binding will cause a location print if user left clicks a section
        self.canvas.bind("<Button-1>", self.leftClick) #binds event to board
        #this binding will call a key event handler function
        self.canvas.bind_all("<Left>", self.LeftHandler)
        self.canvas.bind_all("<Right>", self.RightHandler)
        self.canvas.bind_all("<Up>", self.UpHandler)
        self.canvas.bind_all("<Down>", self.DownHandler)
        self.canvas.bind_all("<F1>", self.QuitHandler)
        
    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        itemID = self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        #print(name)
        #print(self.pieces)
        self.placepiece(name, row, column, itemID)
        

    def placepiece(self, name, row, column, itemID):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column, itemID)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        player_tuple = self.pieces.get("player2") #get player tuple from dict in form (row, col, itemID)
        row_player = player_tuple[0]
        col_player = player_tuple[1]

        player_tuple5 = self.pieces.get("player1") #get player tuple from dict in form (row, col, itemID)
        row_player5 = player_tuple[0]
        col_player5 = player_tuple[1]

        
        
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square", dash=(5,1))


                if ((abs(row - row_player) == 0 and  abs(col - col_player) == 1)
                    or (abs(row - row_player) == 1 and  abs(col - col_player) == 0)):
                        color5 = '#00ffff'
                        #self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", tags="square", stipple='gray25')
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            if (name == "player2"):
                self.placepiece(name, self.pieces[name][0], self.pieces[name][1], self.pieces[name][2])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def leftClick(self, event): #left click handler
        print("clicked at", event.x, event.y)
        
        if not self.pieces:
            print("no pieces left")
            return
        for name in self.pieces:
            print("pieces before deletion:", self.pieces)
            self.canvas.delete(self.pieces[name][2])
            del self.pieces[name]
            return
    def CheckMove(self, pos):

        if (pos > 7 or pos < 0):
            print("pos: ", pos, "pos % 7", pos % 7, "you hit me")
            return False
        else:
            return True
    def CheckEat(self):

        if (self.pieces.get("player1")[0:2] == self.pieces.get("player2")[0:2]):
            player_tuple = self.pieces.get("player2") #get player tuple from dict in form (row, col, itemID)
            print("Cobra ate you!\nTry again!")
            self.placepiece("player1", randint(0, self.rows-1), randint(0, self.columns-1), self.pieces.get("player1")[2])
            self.placepiece("player2", randint(0, self.rows-1), randint(0, self.columns-1), self.pieces.get("player2")[2])
            

                    
            player_tuple = self.pieces.get("player2") #get player tuple from dict in form (row, col, itemID)
            row_player = player_tuple[0]
            col_player = player_tuple[1]
            for row in range(self.rows):
                for col in range(self.columns):
                    x1 = (col * self.size)
                    y1 = (row * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    if ((abs(row - row_player) == 0 and  abs(col - col_player) == 1)
                        or (abs(row - row_player) == 1 and  abs(col - col_player) == 0)):
                            color5 = '#00ffff'
                            #self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", tags="square", stipple='gray25')

                    
        
    def LeftHandler(self, event):
                
        player_tuple = self.pieces.get("player1") #get player tuple from dict in form (row, col, itemID)
        row = player_tuple[0]
        col = player_tuple[1] - 1
        
        if (self.CheckMove(col)):
            self.placepiece("player1", row, col, player_tuple[2])
            self.CheckEat()
            print(self.pieces.get("player1"))
            self.evaluatePath()
        #placepiece(self, name, row, column, itemID)
        
    def RightHandler(self, event):
        player_tuple = self.pieces.get("player1")
        row = player_tuple[0]
        col = player_tuple[1] + 1
        
        if (self.CheckMove(col)):
            self.placepiece("player1", row, col, player_tuple[2])
            self.CheckEat()
            print(self.pieces.get("player1"))
            self.evaluatePath()
        
    def UpHandler(self, event):
        player_tuple = self.pieces.get("player1")
        row = player_tuple[0] - 1
        col = player_tuple[1]
        
        if (self.CheckMove(row)):
            self.placepiece("player1", row, col, player_tuple[2])
            self.CheckEat()
            print(self.pieces.get("player1"))
            self.evaluatePath()
            
    def DownHandler(self, event):
        player_tuple = self.pieces.get("player1")
        row = player_tuple[0] + 1
        col = player_tuple[1]
        
        if (self.CheckMove(row)):
            self.placepiece("player1", row, col, player_tuple[2])
            self.CheckEat()
            print(self.pieces.get("player1"))
            self.evaluatePath()
            
    def QuitHandler(self, event):
        print("pressed{}".format("f1"))
        quit()
        
    def evaluatePath(self):
        player_row = self.pieces.get("player1")[0]
        player_col = self.pieces.get("player1")[1]
        enemy_row = self.pieces.get("player2")[0]
        enemy_col = self.pieces.get("player2")[1]
        s = make_init_state(self.size, 0, [], [player_row, player_col], [enemy_row, enemy_col])
        goal_state = self.se.search(s, game_goal_fn, heur_min_completion_time)
        path = goal_state.get_path_info()
        print(path)
        
        

# Image comes from the Snake Enemy Kit set which is under a Creative Commons license.
# CC0 1.0 Universal (CC0 1.0)
# For more information see http://opengameart.org/content/snake-enemy-kit-32x32
# Author: kungfu4000
# Title: Snake Enemy Kit 32x32


def start_game():
#     player_norm = '''player_norm.png'''
    player_norm = 'player_norm.gif'
#     player_up = '''player_up.png'''
    player_up = '''player_up.gif'''
    #opponent_girl ='''Girl_Snake_Pixel.png'''
#     opponent = '''Cobra_Pixel.png'''
    opponent = '''Cobra_Pixel.gif'''
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    difficulty = 3000
    
#     player_norm = '''player_norm.png'''
#     player_up = '''player_up.png'''
    #opponent_girl ='''Girl_Snake_Pixel.png'''
#     opponent = '''Cobra_Pixel.png''' #detail_snake.png is more detailed but weak

    player1 = tk.PhotoImage(file=player_norm) #player image
#     player1 = tk.PhotoImage(Image.open(player_norm)) #player image
    player2 = tk.PhotoImage(file=opponent) #opponent image
    #player3 = tk.PhotoImage(file=opponent_girl) #opponent girl image
    player_up = tk.PhotoImage(file=player_up) #player up image
    board.addpiece("player1", player1, 0,0)
    board.addpiece("player2", player2, 2,2)
    #board.addpiece("player3", player3, 1,2)
    difficulty = get_difficulty() #get input string for difficulty
    root.after(0, opponent_move()) #move opponent AI
    root.mainloop()
    
def get_difficulty():
        name = input("Easy, medium, hard?")
        lower_name = name.lower()
        #print("lowered name is:", lower_name)
        
        if (lower_name == 'easy'):
            return 2000
        elif (lower_name == 'medium'):
            return 1500
        else:#we are on hard
            return 1000
            
def search_move():
    #function only implements an ad-hoc A*Search with
    #euclidean heuristics for h(x)
    open_list = []
    player_tuple = board.pieces.get("player1") #get player tuple from dict in form (row, col, itemID)
    row_player = player_tuple[0]
    col_player = player_tuple[1]
    player_tuple2 = board.pieces.get("player2")
    row_player2 = player_tuple2[0]
    col_player2 = player_tuple2[1]
    
    for i in range(1,2):
        for j in range(1,2):
            
            row = player_tuple2[0] + i
            col = player_tuple2[1]
            open_list.append((row,col))
            row = player_tuple2[0] - i
            col = player_tuple2[1]
            open_list.append((row,col))
            row = player_tuple2[0] 
            col = player_tuple2[1] + j
            open_list.append((row,col))
            row = player_tuple2[0]
            col = player_tuple2[1] - j
            open_list.append((row,col))
            
    distance = -1
    expansion_list = {}
    #search open list for least diagonal distance
    for coords in open_list:
        euc_dis = (abs(coords[0] - row_player) + abs(coords[1] - col_player))
        if ((coords[0] < 0 or coords[1] < 0) or (coords[0] > 8 or coords[1] > 8)):
            continue
        expansion_list[(coords)] = euc_dis
        if (euc_dis < distance or distance == -1):
            distance = euc_dis

    #
    #
    #AI CODE
    obstacles_list = []
    s = game.make_init_state(board.rows, 0, obstacles_list,
                                [row_player,col_player], [row_player2,col_player2])
    se = game.SearchEngine('astar', 'full')
    final = game_sample_run.test(se, s, 'None', 'path', game.game_goal_fn)
    # AI CODE
    #
    #
    #
    optimal_move = min(expansion_list, key=expansion_list.get)
    board.placepiece("player2", optimal_move[0], optimal_move[1], player_tuple2[2])
    board.CheckEat()
    
    
def opponent_move():
    player_tuple = board.pieces.get("player2")
    #row = player_tuple[0] + 1
    #col = player_tuple[1]
    #board.placepiece("player2", row, col, player_tuple[2])
    search_move()
    root.after(difficulty, opponent_move)  # reschedule event in 2 seconds

if __name__ == "__main__":
    start_game()

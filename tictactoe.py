class Board:

    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.player_1,self.player_2 = "X","O"   
    
    def display(self):
        print("Player 1 is X")
        print("Player 2 is O\n")
        for r in self.board:
            print()
            for c in r:
                print(c, end = " ")
        print("\n")

    def take_input(self,c):  
        row,col,move = 0,0,0   
        print(f"\nYour Move Player {c}:")
        print("\n")
        while(1):
            self.display()
            move = input()
            if not move.isdigit():
                print(f"\nMove Invalid Player {c}")
                continue
            move = int(move)
            if move < 1 or move > 9: 
                print("\nMove Invalid")
                continue
            if move > 0 and move < 4: row = 1
            if move > 3 and move < 7: row = 2
            if move > 6 and move < 10: row = 3
            col = move - (3*row - 2)
            if isinstance(self.board[row-1][col],str):
                print("\nMove already taken! Choose another")
                continue
            break
        if c == 1: self.board[row-1][col] = self.player_1
        else : self.board[row-1][col] = self.player_2
        return (row-1,col,c)           

  
class Game(Board):

    def __init__(self):
        super().__init__()
        self.row = 0
        self.col = 0
        self.player = 0
        self.value = 0

    def check_board(self):
        for r in self.board:
            for b in r:
                if isinstance(b,int) : return True
        print(f"\nGame Draw\n")
        return False

    def check_row(self):        
        r,c = self.row,self.col
        while c < 3:
            if self.board[r][c] != self.value : return False
            c+=1
        c = self.col
        while c >= 0:
            if self.board[r][c] != self.value : return False
            c -= 1
        print(f"\nPlayer {self.player} Won\n")
        return True

    def check_col(self):
        r, c = self.row, self.col
        while r < 3:
            if self.board[r][c] != self.value : return False
            r += 1
        r = self.row
        while r >= 0:
            if self.board[r][c] != self.value : return False
            r -= 1
        print(f"\nPlayer {self.player} Won\n")
        return True

    def check_diag(self):
        diag1 = str(self.board[0][0]) + str(self.board[1][1]) + str(self.board[2][2])
        diag2 = str(self.board[0][2]) + str(self.board[1][1]) + str(self.board[2][0])
        d1 = all(elem == diag1[0] for elem in diag1)
        d2 = all(elem == diag2[0] for elem in diag2)
        if d1 or d2 : 
            print(f"\nPlayer {self.player} Won\n")
            return True        
        return False 

    def check_game(self):
        if not self.check_board() : return False
        self.value = self.board[self.row][self.col]
        if self.check_row(): return False
        if self.check_col(): return False
        if self.row + self.col == 2 or self.row == self.col: 
            if self.check_diag(): return False
        return True
        

g = Game()
while True:
    r,c,p = g.take_input(1)
    g.row = r
    g.col = c
    g.player = p
    if not g.check_game(): break
    
    r, c, p = g.take_input(2)
    g.row = r
    g.col = c
    g.player = p
    if not g.check_game(): break

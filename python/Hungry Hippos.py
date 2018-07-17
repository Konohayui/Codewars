class Game():
    
    def __init__(self, board):
        self.amount = 0
        self.board = board
        self.ones = []
        for rows in range(0, len(self.board)):
            self.ones.append([False]*len(self.board))
        
    def play(self):
        def check_square(x, y):
            temp = [[x, y]]
            point = 0
            
            while point < len(temp):
                x = temp[point][0]
                y = temp[point][1]
                self.ones[x][y] = True
                
                if x != 0:
                # move left
                    if self.board[x - 1][y] == 1 and self.ones[x - 1][y] == False:
                        self.ones[x - 1][y] == True
                        temp.append([x - 1, y])
                    
                if x < len(self.board) - 1:
                # move right
                    if self.board[x + 1][y] == 1 and self.ones[x + 1][y] == False:
                        self.ones[x + 1][y] == True
                        temp.append([x + 1, y])
                        
                if y != 0:
                # move up 
                   if self.board[x][y - 1] == 1 and self.ones[x][y - 1] == False:
                       self.ones[x][y - 1] == True
                       temp.append([x, y - 1])
                       
                if y < len(self.board) - 1:
                # move down
                    if self.board[x][y + 1] == 1 and self.ones[x][y + 1] == False:
                        self.ones[x][y + 1] == True
                        temp.append([x, y + 1])
                point += 1 
                
            return 1
                    
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board)):
                if self.board[x][y] == 1 and self.ones[x][y] == False:
                    self.amount += check_square(x, y)
                    
        return self.amount

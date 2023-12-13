import numpy as np
#from dokusan import generators as dkgen
class Solve():
#    def generateBoard(self):
#        board = np.array(list(dkgen.random_sudoku(avg_rank = 150)))
#        return board
    def emptySearch(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i,j)    
        return None
    def validate(self,board,num,pos):
        for i in range(len(board[0])): #row
            if board[pos[0]][i] == num and pos[1] != i:
                return False
        for j in range(len(board[0])):
            if board[j][pos[0]] == num and pos[0] != i:
                return False
        boxPosX = pos[1]//3
        boxPosY = pos[0]//3
        for i in range((boxPosY + 3), boxPosY*3 +1):
            for j in range((boxPosX + 3), boxPosX*3 +1):
                if board[i][j] and (i,j) != pos:
                    return False
        return True
    def printArray(self,board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("-----------------------")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")
    def solve(self,board):
        find = Solve.emptySearch(self,board)
        if not find:
            return True
        else:
            y, x = find
        for i in range(1,10):
            if Solve.validate(self,board,i,(y,x)):
                board[y][x] = i
                if Solve.solve(self,board):
                    return True
                board[y][x] = 0
        return False
import numpy as np
board = [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7]
]
board2 = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,0,1,9,0,0,5],
[0,0,0,0,0,0,0,0,0]]
def solve(board):
    find = emptySearch(board)
    if not find:
        return True
    else:
        y, x = find

    for i in range(1,10):
        if validate(board, i, (y, x)):
            board[y][x] = i

            if solve(board):
                return True

            board[y][x] = 0
    return False
def validate(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    boxPosX = pos[1] // 3
    boxPosY = pos[0] // 3
    for i in range(boxPosY*3, boxPosY*3 + 3):
        for j in range(boxPosX * 3, boxPosX*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True
def printArray(board):
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


def emptySearch(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 

    return None
printArray(board2)
solve(board2)
print("")
printArray(board2)